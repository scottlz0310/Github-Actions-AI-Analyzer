# GitHub Actions AI Analyzer - プロジェクト構成

## ディレクトリ構造

```
github-actions-ai-analyzer/
├── src/
│   ├── core/
│   │   ├── analyzer.py                # メインのログ解析エンジン
│   │   ├── log_processor.py          # ログの前処理・クリーニング
│   │   ├── pattern_matcher.py        # エラーパターンマッチング
│   │   ├── context_collector.py      # ワークフロー・リポジトリコンテキスト収集
│   │   └── ai_prompt_optimizer.py    # AI用プロンプト最適化
│   │
│   ├── patterns/
│   │   ├── __init__.py               # パターン統合エクスポート
│   │   ├── dependency_patterns.py    # 依存関係エラーパターン
│   │   ├── permission_patterns.py    # 権限エラーパターン
│   │   ├── environment_patterns.py   # 環境エラーパターン
│   │   ├── network_patterns.py       # ネットワークエラーパターン
│   │   └── syntax_patterns.py        # 構文エラーパターン
│   │
│   ├── languages/
│   │   ├── base.py                   # 基底言語クラス
│   │   ├── python/
│   │   │   ├── patterns.py           # Python特有のエラーパターン
│   │   │   ├── context_parser.py     # requirements.txt, pyproject.toml解析
│   │   │   └── quick_fixes.py        # Python向け修正案
│   │   ├── javascript/
│   │   │   ├── patterns.py           # JavaScript特有のエラーパターン
│   │   │   ├── context_parser.py     # package.json等の解析
│   │   │   └── quick_fixes.py        # よくある修正案
│   │   ├── java/
│   │   │   ├── patterns.py
│   │   │   ├── context_parser.py     # pom.xml, build.gradle解析
│   │   │   └── quick_fixes.py
│   │   └── ...
│   │
│   ├── parsers/
│   │   ├── workflow_parser.py        # GitHub Actionsワークフロー解析
│   │   ├── log_parser.py             # GitHub Actionsログパーサー
│   │   ├── repository_parser.py      # リポジトリメタデータ解析
│   │   └── action_parser.py          # 使用アクションの解析
│   │
│   ├── utils/
│   │   ├── file_utils.py             # ファイル操作ユーティリティ
│   │   ├── string_utils.py           # 文字列処理ユーティリティ
│   │   ├── regex_utils.py            # 正規表現ヘルパー
│   │   └── logger.py                 # ロギング機能
│   │
│   ├── types/
│   │   ├── __init__.py               # 型定義エクスポート
│   │   ├── log_types.py              # ログ関連の型定義
│   │   ├── context_types.py          # コンテキスト関連の型定義
│   │   ├── pattern_types.py          # パターン関連の型定義
│   │   └── analysis_types.py         # 解析結果の型定義
│   │
│   ├── cli/
│   │   ├── __init__.py               # CLI エントリーポイント
│   │   ├── commands/
│   │   │   ├── analyze.py            # analyze コマンド
│   │   │   ├── validate.py           # validate コマンド
│   │   │   └── watch.py              # watch コマンド
│   │   └── utils/
│   │       ├── output_formatter.py   # 出力フォーマッター
│   │       └── progress_bar.py       # プログレスバー
│   │
│   └── __init__.py                   # ライブラリのメインエクスポート
│
├── data/
│   ├── error-database/
│   │   ├── common-errors.json        # よくあるエラーデータベース
│   │   ├── solutions.json            # 既知の解決策データベース
│   │   └── patterns-db.json          # パターンデータベース
│   │
│   └── templates/
│       ├── ai-prompts/
│       │   ├── error-analysis.txt    # エラー解析用プロンプトテンプレート
│       │   ├── solution-generation.txt # 解決策生成用プロンプト
│       │   └── best-practices.txt    # ベストプラクティス用プロンプト
│       │
│       └── reports/
│           ├── markdown-report.hbs   # Markdown レポートテンプレート
│           ├── json-report.hbs       # JSON レポートテンプレート
│           └── html-report.hbs       # HTML レポートテンプレート
│
├── tests/
│   ├── unit/
│   │   ├── core/                     # コア機能のユニットテスト
│   │   ├── patterns/                 # パターンマッチングのテスト
│   │   ├── languages/                # 言語固有機能のテスト
│   │   └── parsers/                  # パーサーのテスト
│   │
│   ├── integration/
│   │   ├── full-analysis.test.ts     # エンドツーエンドテスト
│   │   └── cli.test.ts               # CLI統合テスト
│   │
│   └── fixtures/
│       ├── logs/                     # テスト用ログファイル
│       │   ├── python-errors/
│       │   ├── javascript-errors/
│       │   └── general-errors/
│       │
│       ├── workflows/                # テスト用ワークフローファイル
│       └── repositories/             # テスト用リポジトリ構成
│
├── examples/
│   ├── basic_usage.py                # 基本的な使用例
│   ├── custom_patterns.py            # カスタムパターンの追加例
│   ├── language_specific.py          # 言語固有の解析例
│   └── cli_examples.md               # CLI使用例
│
├── docs/
│   ├── api/                          # API ドキュメント
│   ├── guides/                       # 使用ガイド
│   ├── patterns/                     # パターン定義ガイド
│   └── contributing.md               # 貢献ガイド
│
├── scripts/
│   ├── build.py                      # ビルドスクリプト
│   ├── test.py                       # テストスクリプト
│   └── update_patterns.py            # パターンデータベース更新
│
├── pyproject.toml
├── requirements.txt
├── setup.py
├── package.json
├── tsconfig.json
├── jest.config.js
├── .eslintrc.js
├── .prettierrc
├── README.md
└── CHANGELOG.md
```

## 主要ファイルの役割

### コア機能

- **analyzer.py**: メインAPIとオーケストレーション
- **log_processor.py**: ログのクリーニングとノイズ除去
- **pattern_matcher.py**: エラーパターンの検出とマッチング
- **ai_prompt_optimizer.py**: AI向けの最適化されたプロンプト生成

### 拡張性を考慮した設計

- **languages/**: 言語固有のロジックを分離
- **patterns/**: エラーパターンをカテゴリ別に整理
- **data/**: 設定やテンプレートを外部ファイル化

### 使いやすさ

- **cli/**: コマンドライン インターフェース
- **examples/**: 実用的な使用例
- **docs/**: 充実したドキュメント

この構成により、機能追加や新しい言語サポートが容易になり、保守性の高いライブラリが実現できます。
