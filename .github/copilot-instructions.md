# GitHub Actions AI Analyzer – AIエージェント向けガイド

## アーキテクチャ

- 目的: GitHub ActionsのログやCIレポートを構造化し、AIが改善案を提案できる形に整えるライブラリ兼CLIです。
- 主要パイプライン: `cli/main.py` → `core/analyzer.GitHubActionsAnalyzer` → `LogProcessor` (前処理) → `PatternMatcher` (既知パターン検出) → `ContextCollector` (リポジトリ/ワークフロー情報収集) → `AIPromptOptimizer` (AI向けプロンプト整形)。
- データモデルは `src/github_actions_ai_analyzer/types/` のPydanticモデルで統一され、列挙型(`LogLevel`, `PatternCategory`など)が文字列値を返す点に注意して実装・テストします。

## コアコードの着目点

- `LogProcessor` はノイズ除去正規表現とログレベル推定ロジックを内包し、回帰を防ぐため `tests/unit/core/test_log_processor.py` を更新必須です。
- `PatternMatcher` の既定パターンは正規表現文字列で記述され、信頼度0.5超のみ採用します。パターン追加時は`PatternCategory`列挙に適切なカテゴリを使い、対応するテストを `tests/unit/core/test_pattern_matcher.py` に追加してください。
- `ContextCollector` はファイルシステム探索とYAML解析を行い、外部環境コール(subprocess)をモック化したテストが揃っています。I/Oを伴う変更はテスト側のFixturesも更新しましょう。
- `AIPromptOptimizer` は生成テンプレートを文字列フォーマットで保持し、解析結果(`AnalysisResult`)をもとにMarkdown調の文字列を返します。テンプレート変更は期待文字列を比較するテストを壊しやすいため慎重に調整してください。

## CLI / ツール

- CLIエントリ `gh-actions-analyzer` は Click で構築され、`analyze`, `validate`, `watch` サブコマンドを提供します。ビュー層(リッチテーブル／パネル)は `_display_*` 関数群に分離されています。
- CLIやスクリプトの起動は `uv run gh-actions-analyzer ...` や `uv run tools/github_actions_ai_analyzer_enhanced.py` のように `uv run` を介して行い、仮想環境を明示的にアクティブ化しない運用に統一します。
- `validate` コマンドでは `_check_timeout_settings` や `_check_permissions` など固有のベストプラクティス判定があり、非推奨アクションはリスト上位3件まで報告します。
- `tools/github_actions_ai_analyzer_enhanced.py` はCIレポート解析と品質メトリクス計算をまとめたスクリプトです。CLI本体とロジックが別系統で維持されている点を踏まえて、共通化する際は重複パターン対応を意識してください。

## テストと品質

- 依存関係は `uv sync --all-groups` で同期します。任意のPythonスクリプトやCLIは `uv run <cmd>` で実行し、環境差異を避けます。
- 単体テスト: `uv run pytest`。カバレッジ付きは `uv run pytest --cov=src/github_actions_ai_analyzer --cov-report=term-missing --cov-report=html`。`pyproject.toml` の `[tool.pytest.ini_options]` で常にカバレッジと `--strict-config` が有効です。
- リント/フォーマット: `uv run ruff check src tests examples` と `uv run ruff format src tests examples`。既存ルールは `ruff.toml`（未作成の場合は追加）に集約します。
- 型チェック: `uv run mypy src`。mypyはstrict設定であり、新規モジュールにも型注釈と日本語Docstringを揃えます。
- Pythonサポートは3.12+に統一。旧バージョン互換コード（typing_extensions等）は段階的に整理し、必要ならガードを明示してください。

## バージョン/リリース

- バージョン更新は `.cursorrules` に従い `pyproject.toml`, `docs/conf.py`, `src/github_actions_ai_analyzer/__init__.py`, `cli/main.py`, `README.md`, `CHANGELOG.md` を同期させます。スクリプトは `uv run scripts/bump_version.py X.Y.Z` で起動します。
- 公開フローは `uv run python -m build` → `uv run twine upload` を基本とし、`publish`/`publish-prod` ターゲットに組み込む際も `uv run` 経由で実行します。

## 作業時の注意

- コードとdocstringは型ヒント必須・日本語Docstring推奨( `.cursorrules` )。既存スタイルに合わせてDocstringを日本語で追加・修正してください。
- 新規パターンや解析ロジック追加時は、サマリー生成(`_generate_summary`)・推奨事項(`_generate_recommendations`)への影響も確認し、必要なら`tests/unit/core/test_analyzer.py`の期待値を更新します。
- CLIのリッチ出力は視覚テストが難しいため、テーブル構造変更時は文字列比較ではなくカラム存在検証を行う形でテストを追加します。
- `_is_tool_available` は許可されたコマンドだけをチェックする安全設計です。新しいツールを追加する場合は許可リストとモックテストの両方を更新してください。
- `watch` コマンドは未実装のTODOが残っています。監視機能を追加する場合はファイル変更検知のポーリング/通知をテストしやすい形で抽象化しましょう。
- 大規模変更を行う際は `uv run ruff check`, `uv run mypy src`, `uv run pytest --cov=src/github_actions_ai_analyzer`, `uv run bandit -r src` など主要ゲートをまとめて通してからPRを作成してください。
