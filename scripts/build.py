#!/usr/bin/env python3
"""
ビルドスクリプト

PyPIパッケージのビルドとテストを行います。
"""

import shutil
import subprocess  # nosec B404
import sys
from pathlib import Path


def run_command(command: str, description: str) -> bool:
    """コマンドを実行"""
    print(f"🔄 {description}...")
    # コマンドをリストに分割してshell=Trueを避ける
    command_list = command.split() if isinstance(command, str) else command
    result = subprocess.run(  # nosec B603
        command_list, shell=False, capture_output=True, text=True
    )

    if result.returncode != 0:
        print(f"❌ {description} に失敗しました:")
        print(result.stderr)
        return False

    print(f"✅ {description} が完了しました")
    if result.stdout.strip():
        print(result.stdout)
    return True


def clean_build():
    """ビルドディレクトリをクリーンアップ"""
    print("🧹 ビルドディレクトリをクリーンアップ...")

    dirs_to_clean = ["build", "dist", "*.egg-info"]
    for pattern in dirs_to_clean:
        for path in Path(".").glob(pattern):
            if path.is_dir():
                shutil.rmtree(path)
                print(f"  削除: {path}")
            elif path.is_file():
                path.unlink()
                print(f"  削除: {path}")

    print("✅ クリーンアップが完了しました")


def run_tests():
    """テストを実行"""
    return run_command("pytest tests/ -v", "テスト実行")


def run_linting():
    """リンティングを実行"""
    commands = [
        ("black --check src/ tests/", "Black フォーマットチェック"),
        ("isort --check-only src/ tests/", "isort インポートチェック"),
        ("flake8 src/ tests/", "flake8 リンティング"),
    ]

    for command, description in commands:
        if not run_command(command, description):
            return False
    return True


def run_type_checking():
    """型チェックを実行"""
    return run_command("mypy src/", "mypy 型チェック")


def build_package():
    """パッケージをビルド"""
    return run_command("python -m build", "パッケージビルド")


def test_package():
    """ビルドされたパッケージをテスト"""
    # ソースディストリビューションをテスト
    sdist_files = list(Path("dist").glob("*.tar.gz"))
    if sdist_files:
        return run_command(
            f"pip install {sdist_files[0]} --force-reinstall",
            "ソースディストリビューションのテスト",
        )

    # ホイールをテスト
    wheel_files = list(Path("dist").glob("*.whl"))
    if wheel_files:
        return run_command(
            f"pip install {wheel_files[0]} --force-reinstall",
            "ホイールのテスト",
        )

    print("❌ ビルドファイルが見つかりません")
    return False


def main():
    """メイン関数"""
    print("🚀 GitHub Actions AI Analyzer ビルドスクリプト")
    print("=" * 50)

    # 現在のディレクトリを確認
    if not Path("pyproject.toml").exists():
        print(
            "❌ pyproject.toml が見つかりません。プロジェクトルートで実行してください。"
        )
        sys.exit(1)

    # クリーンアップ
    clean_build()

    # テスト実行
    if not run_tests():
        print("❌ テストが失敗しました")
        sys.exit(1)

    # リンティング
    if not run_linting():
        print("❌ リンティングが失敗しました")
        sys.exit(1)

    # 型チェック
    if not run_type_checking():
        print("❌ 型チェックが失敗しました")
        sys.exit(1)

    # パッケージビルド
    if not build_package():
        print("❌ パッケージビルドが失敗しました")
        sys.exit(1)

    # パッケージテスト
    if not test_package():
        print("❌ パッケージテストが失敗しました")
        sys.exit(1)

    print("\n🎉 すべてのビルドステップが完了しました！")
    print("\n📦 ビルドされたファイル:")
    for file in Path("dist").glob("*"):
        print(f"  - {file}")


if __name__ == "__main__":
    main()
