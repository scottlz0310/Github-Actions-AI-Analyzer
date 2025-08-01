# GitHub Actions AI Analyzer

GitHub Actionsのエラーログを解析し、AIによる改善案生成を支援するライブラリ・ツールです。

## 概要

GitHub Actionsのワークフロー実行で発生するエラーログは、大量のノイズを含み、AIが根本原因を特定するのが困難です。このツールは、エラーログを構造化・最適化し、AIによる効果的な改善案生成を支援します。

## 主な機能

- **ログ解析エンジン**: GitHub Actionsの生ログを解析し、構造化されたエラー情報を抽出
- **パターンマッチングシステム**: 既知のエラーパターンとのマッチングによる高速な原因特定
- **コンテキスト収集システム**: エラーの背景情報を収集し、AI解析の精度向上に寄与
- **AI プロンプト最適化エンジン**: 構造化されたエラー情報をAIが理解しやすい形式に変換

## 対応言語・フレームワーク

- **Python**: pip, poetry, venv, Django, Flask
- **JavaScript/Node.js**: npm, yarn, pnpm, React, Vue, Next.js
- **Java**: Maven, Gradle, Spring Boot

## インストール

```bash
pip install github-actions-ai-analyzer
```

## 使用方法

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
```

### CLI の使用

```bash
# ログファイルを解析
gh-actions-analyzer analyze log.txt

# ワークフローファイルを指定して解析
gh-actions-analyzer analyze log.txt -w .github/workflows/ci.yml

# JSON形式で出力
gh-actions-analyzer analyze log.txt -o json

# 最小ログレベルを指定
gh-actions-analyzer analyze log.txt -l error
```

## 開発

### セットアップ

```bash
git clone https://github.com/scottlz0310/Github-Actions-AI-Analyzer.git
cd Github-Actions-AI-Analyzer
pip install -e ".[dev]"
```

### テスト

```bash
pytest
```

### コードフォーマット

```bash
black src/
isort src/
```

## ライセンス

MIT License

## 貢献

プルリクエストやイシューの報告を歓迎します。詳しくは[CONTRIBUTING.md](CONTRIBUTING.md)をご覧ください。 