.PHONY: help install install-dev test test-cov lint format type-check security-check clean build publish docs

help: ## このヘルプメッセージを表示
	@echo "利用可能なコマンド:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## プロジェクトをインストール
	pip install -e .

install-dev: ## 開発用依存関係をインストール
	pip install -e ".[dev]"
	pre-commit install

test: ## テストを実行
	pytest tests/ -v

test-cov: ## カバレッジ付きでテストを実行
	pytest tests/ --cov=src/ --cov-report=html --cov-report=term-missing -v

lint: ## コードの品質チェックを実行
	flake8 src/ tests/ examples/
	black --check --diff src/ tests/ examples/
	isort --check-only --diff src/ tests/ examples/

format: ## コードを自動フォーマット
	black src/ tests/ examples/
	isort src/ tests/ examples/

type-check: ## 型チェックを実行
	mypy src/

security-check: ## セキュリティチェックを実行
	bandit -r src/
	safety check

clean: ## キャッシュとビルドファイルを削除
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	rm -rf build/
	rm -rf dist/
	rm -rf htmlcov/
	rm -f .coverage
	rm -f coverage.xml

build: ## パッケージをビルド
	python -m build

publish: ## PyPIにパッケージを公開（テスト用）
	twine upload --repository testpypi dist/*

publish-prod: ## PyPIにパッケージを公開（本番用）
	twine upload dist/*

docs: ## ドキュメントを生成
	cd docs && make html

check-all: ## すべてのチェックを実行
	make lint
	make type-check
	make security-check
	make test-cov

ci: ## CI/CDパイプライン用のチェック
	make check-all
	make build
