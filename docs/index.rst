GitHub Actions AI Analyzer Documentation
========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   quickstart
   api
   cli
   examples
   contributing

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Welcome to GitHub Actions AI Analyzer's documentation!
=====================================================

GitHub Actionsのエラーログを解析し、AIによる改善案生成を支援するライブラリ・ツールです。

主な機能
--------

* **ログ解析エンジン**: GitHub Actionsの生ログを解析し、構造化されたエラー情報を抽出
* **パターンマッチングシステム**: 既知のエラーパターンとのマッチングによる高速な原因特定
* **コンテキスト収集システム**: エラーの背景情報を収集し、AI解析の精度向上に寄与
* **AI プロンプト最適化エンジン**: 構造化されたエラー情報をAIが理解しやすい形式に変換
* **多言語対応**: Python、JavaScript、Javaのエラーパターンに対応
* **豊富な出力形式**: テキスト、JSON、YAML形式での結果出力

対応言語・フレームワーク
-----------------------

Python
^^^^^^
* **パッケージマネージャー**: pip, poetry, venv
* **フレームワーク**: Django, Flask, FastAPI
* **エラーパターン**: ModuleNotFoundError, ImportError, pip install failures

JavaScript/Node.js
^^^^^^^^^^^^^^^^^
* **パッケージマネージャー**: npm, yarn, pnpm
* **フレームワーク**: React, Vue, Next.js, Express
* **エラーパターン**: npm install failures, module resolution errors

Java
^^^^
* **ビルドツール**: Maven, Gradle
* **フレームワーク**: Spring Boot, Jakarta EE
* **エラーパターン**: Compilation errors, dependency conflicts

インストール
-----------

.. code-block:: bash

   pip install github-actions-ai-analyzer

クイックスタート
---------------

.. code-block:: python

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

詳細な使用方法については、:doc:`quickstart` を参照してください。 