#!/usr/bin/env python3
"""
PyPI公開スクリプト

PyPIにパッケージを公開します。
"""

import sys
import subprocess
from pathlib import Path


def run_command(command, description):
    """コマンドを実行"""
    print(f"🔄 {description}...")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"❌ {description} に失敗しました:")
        print(result.stderr)
        return False
    
    print(f"✅ {description} が完了しました")
    if result.stdout.strip():
        print(result.stdout)
    return True


def check_build_files():
    """ビルドファイルの存在を確認"""
    dist_dir = Path('dist')
    if not dist_dir.exists():
        print("❌ dist/ ディレクトリが見つかりません。先にビルドを実行してください。")
        return False
    
    files = list(dist_dir.glob('*'))
    if not files:
        print("❌ ビルドファイルが見つかりません。先にビルドを実行してください。")
        return False
    
    print("📦 ビルドファイル:")
    for file in files:
        print(f"  - {file}")
    
    return True


def check_twine():
    """twineがインストールされているか確認"""
    try:
        subprocess.run(["twine", "--version"], 
                      capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ twine がインストールされていません。")
        print("   インストール: pip install twine")
        return False


def check_pypi_config():
    """PyPI設定を確認"""
    home = Path.home()
    pypirc = home / '.pypirc'
    
    if not pypirc.exists():
        print("⚠️  ~/.pypirc ファイルが見つかりません。")
        print("   PyPIアカウントの設定が必要です。")
        print("   ファイル例:")
        print("   [distutils]")
        print("   index-servers =")
        print("       pypi")
        print("       testpypi")
        print("   [pypi]")
        print("   repository = https://upload.pypi.org/legacy/")
        print("   username = your-username")
        print("   password = your-password")
        return False
    
    return True


def test_upload():
    """TestPyPIにアップロードテスト"""
    print("\n🧪 TestPyPIにアップロードテスト...")
    
    if not run_command("twine upload --repository testpypi dist/*", 
                      "TestPyPIアップロード"):
        return False
    
    print("\n✅ TestPyPIアップロードが完了しました")
    print("   テスト用URL: https://test.pypi.org/project/github-actions-ai-analyzer/")
    return True


def production_upload():
    """本番PyPIにアップロード"""
    print("\n🚀 本番PyPIにアップロード...")
    
    # 確認プロンプト
    response = input("本番PyPIにアップロードしますか？ (y/N): ")
    if response.lower() != 'y':
        print("❌ アップロードをキャンセルしました")
        return False
    
    if not run_command("twine upload dist/*", "PyPIアップロード"):
        return False
    
    print("\n🎉 PyPIアップロードが完了しました！")
    print("   パッケージURL: https://pypi.org/project/github-actions-ai-analyzer/")
    return True


def main():
    """メイン関数"""
    print("🚀 GitHub Actions AI Analyzer PyPI公開スクリプト")
    print("=" * 50)
    
    # 現在のディレクトリを確認
    if not Path('pyproject.toml').exists():
        print("❌ pyproject.toml が見つかりません。プロジェクトルートで実行してください。")
        sys.exit(1)
    
    # twineの確認
    if not check_twine():
        sys.exit(1)
    
    # ビルドファイルの確認
    if not check_build_files():
        sys.exit(1)
    
    # PyPI設定の確認
    if not check_pypi_config():
        print("\n⚠️  PyPI設定を確認してから再実行してください。")
        sys.exit(1)
    
    # TestPyPIアップロード
    if not test_upload():
        sys.exit(1)
    
    # 本番アップロード
    if not production_upload():
        sys.exit(1)
    
    print("\n🎉 パッケージの公開が完了しました！")
    print("\n📋 次のステップ:")
    print("1. PyPIでパッケージを確認: https://pypi.org/project/github-actions-ai-analyzer/")
    print("2. インストールテスト: pip install github-actions-ai-analyzer")
    print("3. GitHubリリースを作成")
    print("4. ドキュメントを更新")


if __name__ == "__main__":
    main() 