# GitHub Actions AI Analyzer

[![PyPI version](https://badge.fury.io/py/github-actions-ai-analyzer.svg)](https://badge.fury.io/py/github-actions-ai-analyzer)
[![Version](https://img.shields.io/badge/version-0.1.6-blue.svg)](https://github.com/scottlz0310/Github-Actions-AI-Analyzer/releases/tag/v0.1.4)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![AI Quality](https://img.shields.io/badge/AI%20Quality-Enhanced-brightgreen.svg)](https://github.com/scottlz0310/Github-Actions-AI-Analyzer)

GitHub Actionsのエラーログを解析し、AIによる改善案生成を支援するライブラリ・ツールです。

## 🤖 AI品質向上システム統合

このリポジトリには、PhotoGeoViewプロジェクトで開発された**AI品質向上システム**が統合されています。自動的なテスト品質向上と継続的な改善を支援します。

### 🎯 AI品質向上システムの機能

- **自動品質解析**: CIレポートとログファイルの自動解析
- **品質メトリクス計算**: 総合品質スコアの算出
- **改善提案生成**: 具体的な修正アクションの提案
- **自動修正実行**: コードフォーマットの自動修正
- **品質レポート生成**: 包括的な品質レポートの生成

### 📊 品質メトリクス

- **総合品質スコア**: プロジェクト全体の品質評価
- **エラー頻度**: 1000行あたりのエラー数
- **警告頻度**: 1000行あたりの警告数
- **問題密度**: コードの問題密度

### 🚀 使用方法

```bash
# AI品質向上システムの実行
python tools/github_actions_ai_analyzer_enhanced.py

# GitHub Actionsワークフローの実行
# .github/workflows/ai-quality-improvement.yml
```

詳細については、[AI品質統合ガイド](docs/ai_quality_integration_guide.md)をご覧ください。

## 📖 概要

GitHub Actionsのワークフロー実行で発生するエラーログは、大量のノイズを含み、AIが根本原因を特定するのが困難です。このツールは、エラーログを構造化・最適化し、AIによる効果的な改善案生成を支援します。

### 🎯 解決する課題

- **ログのノイズ除去**: セットアップログ、無関係な警告の除去
- **エラーの構造化**: 散在するエラー情報の統合と分類
- **コンテキスト情報の補完**: ワークフロー構成、リポジトリ情報との関連付け
- **AI向け最適化**: AIが理解しやすい形でのプロンプト生成

## ✨ 主な機能

- **ログ解析エンジン**: GitHub Actionsの生ログを解析し、構造化されたエラー情報を抽出
- **パターンマッチングシステム**: 既知のエラーパターンとのマッチングによる高速な原因特定
- **コンテキスト収集システム**: エラーの背景情報を収集し、AI解析の精度向上に寄与
- **AI プロンプト最適化エンジン**: 構造化されたエラー情報をAIが理解しやすい形式に変換
- **多言語対応**: Python、JavaScript、Javaのエラーパターンに対応
- **豊富な出力形式**: テキスト、JSON、YAML形式での結果出力

## 🛠️ 対応言語・フレームワーク

### Python
- **パッケージマネージャー**: pip, poetry, venv
- **フレームワーク**: Django, Flask, FastAPI
- **エラーパターン**: ModuleNotFoundError, ImportError, pip install failures

### JavaScript/Node.js
- **パッケージマネージャー**: npm, yarn, pnpm
- **フレームワーク**: React, Vue, Next.js, Express
- **エラーパターン**: npm install failures, module resolution errors

### Java
- **ビルドツール**: Maven, Gradle
- **フレームワーク**: Spring Boot, Jakarta EE
- **エラーパターン**: Compilation errors, dependency conflicts

## 🚀 インストール

```bash
# 最新バージョンをインストール
pip install github-actions-ai-analyzer

# 特定のバージョンをインストール
pip install github-actions-ai-analyzer==0.1.6

# AI品質向上システム付きでインストール
pip install github-actions-ai-analyzer[ai-quality]
```

## 🔧 開発環境のセットアップ

### 前提条件
- Python 3.8+
- Git
- Make（オプション）

### セットアップ手順

```bash
# リポジトリをクローン
git clone https://github.com/scottlz0310/Github-Actions-AI-Analyzer.git
cd Github-Actions-AI-Analyzer

# 仮想環境を作成
python -m venv venv
source venv/bin/activate  # Linux/macOS
# または
venv\Scripts\activate  # Windows

# 開発用依存関係をインストール
make install-dev
# または
pip install -e ".[dev]"
pre-commit install
```

### 開発用コマンド

```bash
# ヘルプを表示
make help

# コードの品質チェック
make lint

# コードを自動フォーマット
make format

# 型チェック
make type-check

# セキュリティチェック
make security-check

# テストを実行
make test

# カバレッジ付きでテストを実行
make test-cov

# すべてのチェックを実行
make check-all

# パッケージをビルド
make build

# キャッシュをクリア
make clean
```

## 📚 使用方法

### 基本的な使用例

```python
from github_actions_ai_analyzer import GitHubActionsAnalyzer
from github_actions_ai_analyzer.types import LogLevel

# アナライザーを作成
analyzer = GitHubActionsAnalyzer()

# ログファイルを解析
result = analyzer.analyze_log_file(
    log_file_path="path/to/log.txt",
    workflow_file_path=".github/workflows/ci.yml",
    repository_path=".",
    min_log_level=LogLevel.WARNING
)

# 結果を表示
print(result.summary)
for error in result.error_analyses:
    print(f"エラー: {error.root_cause}")
    print(f"重要度: {error.severity}")
    print(f"影響ステップ: {', '.join(error.affected_steps)}")

# 解決策を表示
for solution in result.solution_proposals:
    print(f"解決策: {solution.title}")
    print(f"信頼度: {solution.confidence:.1%}")
```

### CLI の使用

```bash
# 基本的なログファイル解析
gh-actions-analyzer analyze log.txt

# ワークフローファイルを指定して解析
gh-actions-analyzer analyze log.txt -w .github/workflows/ci.yml

# リポジトリパスを指定
gh-actions-analyzer analyze log.txt -r /path/to/repository

# JSON形式で出力
gh-actions-analyzer analyze log.txt -o json

# 最小ログレベルを指定（error以上のみ）
gh-actions-analyzer analyze log.txt -l error

# ワークフローファイルを検証
gh-actions-analyzer validate .github/workflows/ci.yml

# 複数のワークフローファイルを検証
gh-actions-analyzer validate .github/workflows/security.yml
gh-actions-analyzer validate .github/workflows/release.yml

# ヘルプを表示
gh-actions-analyzer --help
```

### ワークフローファイル検証機能

**検証項目**:
- ✅ YAML構文の妥当性
- ✅ 必須フィールド（name、on、jobs）の存在
- ✅ ジョブ名の重複チェック
- ✅ ステップ構造の検証
- ⚠️ ベストプラクティス（タイムアウト設定、権限設定）

**検証結果例**:
```
ワークフローファイル検証結果
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ 項目               ┃ 状態    ┃ 詳細                                                                               ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ YAML構文           │ ✅ 正常 │ 有効なYAML形式です                                                                 │
│ 必須フィールド     │ ✅ 正常 │ すべての必須フィールドが存在します: name, on, jobs                                 │
│ ジョブ数           │ ✅ 正常 │ 9個のジョブが定義されています                                                      │
│ ジョブ名重複       │ ✅ 正常 │ 重複したジョブ名はありません                                                       │
│ ベストプラクティス │ ⚠️ 警告  │ 一部のジョブにタイムアウト設定がありません                                       │
└────────────────────┴─────────┴────────────────────────────────────────────────────────────────────────────────────┘
```

### 出力例

```
GitHub Actions AI Analyzer
ログファイル: /path/to/log.txt

解析結果:
解析ID: 12345678-1234-1234-1234-123456789abc
サマリー: 合計3個のエラーが検出され、2個の解決策が提案されました。

エラー分析数: 3
エラー 1:
  ID: error_dep_missing_package_0
  根本原因: Pythonパッケージが見つからない
  重要度: error
  影響ステップ: Install dependencies
  関連ファイル: *.py

解決策提案数: 2
解決策 1:
  タイトル: Missing Packageの解決
  説明: Pythonパッケージが見つからないを解決するための手順
  信頼度: 70.0%
  推定時間: 5-10分
```

## 🔧 開発

### セットアップ

```bash
# リポジトリをクローン
git clone https://github.com/scottlz0310/Github-Actions-AI-Analyzer.git
cd Github-Actions-AI-Analyzer

# 開発環境をセットアップ
pip install -e ".[dev]"

# プリコミットフックをインストール
pre-commit install
```

### テスト

```bash
# 全テストを実行
pytest

# カバレッジ付きでテスト実行
pytest --cov=src/github_actions_ai_analyzer

# 特定のテストファイルを実行
pytest tests/unit/test_log_processor.py
```

### コード品質

```bash
# コードフォーマット
black src/ tests/

# インポートソート
isort src/ tests/

# リンティング
flake8 src/ tests/

# 型チェック
mypy src/
```

### 使用例の実行

```bash
# 基本的な使用例を実行
python examples/basic_usage.py
```

## 📋 エラーパターン

### 依存関係エラー
- パッケージの不整合
- バージョン競合
- インストール失敗

### 権限エラー
- ファイルアクセス権限
- 実行権限の問題

### 環境エラー
- コマンド不足
- PATH設定の問題
- バージョン不一致

### ネットワークエラー
- タイムアウト
- 接続エラー
- DNS解決失敗

### 構文エラー
- YAML構文エラー
- JSON構文エラー
- スクリプト構文エラー

## 🤝 貢献

プルリクエストやイシューの報告を歓迎します！

### 貢献の流れ

1. このリポジトリをフォーク
2. 機能ブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを作成

詳しくは[CONTRIBUTING.md](CONTRIBUTING.md)をご覧ください。

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳しくは[LICENSE](LICENSE)ファイルをご覧ください。

## 🙏 謝辞

- [GitHub Actions](https://github.com/features/actions) - CI/CDプラットフォーム
- [Pydantic](https://pydantic-docs.helpmanual.io/) - データバリデーション
- [Click](https://click.palletsprojects.com/) - CLIフレームワーク
- [Rich](https://rich.readthedocs.io/) - ターミナル出力

## 📞 サポート

- **Issues**: [GitHub Issues](https://github.com/scottlz0310/Github-Actions-AI-Analyzer/issues)
- **Discussions**: [GitHub Discussions](https://github.com/scottlz0310/Github-Actions-AI-Analyzer/discussions)
- **Email**: scottlz0310@gmail.com

## 🔄 CI/CDパイプライン

このプロジェクトは包括的なCI/CDパイプラインを採用しており、コード品質とセキュリティを自動的に保証します。

### 🏗️ パイプライン構成

#### コード品質チェック
- **Black**: コードフォーマット
- **isort**: インポート文の整理
- **Flake8**: リンティング
- **MyPy**: 型チェック
- **Pre-commit**: コミット前チェック

#### テスト実行
- **Unit Tests**: 単体テスト（pytest）
- **Integration Tests**: 統合テスト
- **Coverage**: テストカバレッジ（80%以上要求）
- **Multi-platform**: Ubuntu, Windows, macOS
- **Multi-version**: Python 3.8-3.12

#### セキュリティスキャン
- **CodeQL**: GitHubの静的解析
- **Bandit**: Pythonセキュリティスキャン
- **Safety**: 依存関係の脆弱性チェック
- **Trivy**: コンテナ・ファイルシステムスキャン
- **Dependency Review**: 依存関係の変更レビュー

#### 自動化
- **Dependabot**: 依存関係の自動更新
- **Release Management**: 自動リリース作成
- **PyPI Deployment**: 自動パッケージ公開
- **Documentation**: 自動ドキュメント生成

### 📊 品質メトリクス

#### 現在のバージョン
- **Version**: 0.1.4
- **Release Date**: 2024-08-02
- **Python Support**: 3.8+

#### テストカバレッジ
- **Overall Coverage**: 80%+（目標）
- **Core Modules**: 
  - PatternMatcher: 100%
  - ContextCollector: 92%
  - Analyzer: 84%
  - LogProcessor: 67%

#### セキュリティ
- **Vulnerabilities**: 0（目標）
- **Security Score**: A+（目標）
- **Dependency Updates**: 自動化済み

### 🚀 対応状況
- ✅ 基本的なログ解析機能
- ✅ エラーパターンマッチング
- ✅ CLIインターフェース
- ✅ 多言語対応（Python, JavaScript, Java）
- ✅ テストフレームワーク
- ✅ CI/CDパイプライン
- ✅ セキュリティスキャン
- ✅ 自動リリース管理
- 🔄 AIプロンプト最適化（開発中）
- 🔄 統合テスト（開発中）

---

⭐ このプロジェクトが役に立ったら、スターを付けてください！ 