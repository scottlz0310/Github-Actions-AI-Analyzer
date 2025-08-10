# ログの自動収集と機械学習による改善提案

## 🧭 プロジェクト概要

**目的**
GitHub Actions のログを自動収集・解析し、構造的な意味を抽出。
さらに、過去のログと対応履歴を学習し、次回以降の判断を支援する。

**思想**

- Helper文化：未来の自分や他者を助ける構造的設計
- ritual-log：必要な記録だけを残し、意味を持たせる
- 自動化と構造美の両立

---

## 🧱 機能構成

| 機能                 | 説明                                                  |
| -------------------- | ----------------------------------------------------- |
| ログ収集             | GitHub Actions のログを API 経由で取得（run_id 指定） |
| ログ解析             | エラー分類・意味抽出・改善提案の生成                  |
| レポート出力         | JSON形式で構造化された解析結果を保存                  |
| PRコメント           | 結果を PR に自動コメント（判断支援）                  |
| 学習機能             | 過去ログと対応履歴を蓄積・分類・予測                  |
| フィードバックループ | 人間の対応結果を学習に反映                            |

---

## 🔄 ワークフロー統合例（GitHub Actions）

```yaml
name: Analyze Logs

on: [push, pull_request]

jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Install analyzer
        run: pip install github-actions-ai-analyzer

      - name: Run analyzer
        run: |
          python -m github_actions_ai_analyzer \
            --run-id ${{ github.run_id }} \
            --output report.json

      - name: Post result
        run: python scripts/post_comment.py report.json
```

---

## 🧠 学習機能の構想

### 学習対象

- ログの種類（例：flake8, pytest, build error）
- 発生箇所・頻度・コンテキスト
- 人間の対応（修正内容・ignore設定・再実行）

### データ形式（例）

```json
{
  "log": "flake8: E501 line too long",
  "context": "theme_manager.py:42",
  "resolution": "ignore E501 in config",
  "confidence": 0.92
}
```

### モデル案

- 類似ログ検索：`sentence-transformers`
- 判断予測：`RandomForestClassifier`（軽量・解釈性あり）

---

## 🪶 哲学的設計指針

- **意味のあるログだけを残す**（ritual-log）
- **人間が見る前に構造化する**
- **判断基準を継承・進化させる**
- **自動化は「助ける」ためにある**

---

## 🛠 次のステップ

1. ログ収集・解析 CLI の整備（run_id 指定）
2. PRコメント出力のテンプレート化
3. 学習データの形式設計と収集開始
4. 軽量モデルによる提案機能の試作
5. GitHub Action 化と `.yml` テンプレート提供

---
