#!/usr/bin/env python3
"""
バージョン番号一括更新スクリプト

使用方法:
    python scripts/bump_version.py 0.1.5
"""

import re
import sys
from pathlib import Path

def update_file_version(file_path: Path, old_version: str, new_version: str) -> bool:
    """ファイル内のバージョン番号を更新"""
    try:
        content = file_path.read_text(encoding='utf-8')
        updated = False
        
        # パターンマッチング
        patterns = [
            (rf'version\s*=\s*["\']{re.escape(old_version)}["\']', f'version = "{new_version}"'),
            (rf'__version__\s*=\s*["\']{re.escape(old_version)}["\']', f'__version__ = "{new_version}"'),
            (rf'release\s*=\s*["\']{re.escape(old_version)}["\']', f"release = '{new_version}'"),
            (rf'version\s*=\s*["\']{re.escape(old_version)}["\']', f'version = "{new_version}"'),
            (rf'version-{re.escape(old_version)}', f'version-{new_version}'),
            (rf'=={re.escape(old_version)}', f'=={new_version}'),
        ]
        
        for pattern, replacement in patterns:
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                updated = True
        
        if updated:
            file_path.write_text(content, encoding='utf-8')
            print(f"✅ 更新: {file_path}")
            return True
        else:
            print(f"⚠️  変更なし: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ エラー: {file_path} - {e}")
        return False

def main():
    if len(sys.argv) != 2:
        print("使用方法: python scripts/bump_version.py <new_version>")
        print("例: python scripts/bump_version.py 0.1.5")
        sys.exit(1)
    
    new_version = sys.argv[1]
    
    # バージョン形式の検証
    if not re.match(r'^\d+\.\d+\.\d+$', new_version):
        print("❌ エラー: バージョン形式が正しくありません (例: 0.1.5)")
        sys.exit(1)
    
    # 更新対象ファイル
    files_to_update = [
        "pyproject.toml",
        "docs/conf.py",
        "src/github_actions_ai_analyzer/__init__.py",
        "src/github_actions_ai_analyzer/cli/main.py",
        "README.md",
    ]
    
    print(f"🔄 バージョンを {new_version} に更新中...")
    
    updated_count = 0
    for file_path in files_to_update:
        path = Path(file_path)
        if path.exists():
            # 現在のバージョンを検出（簡易版）
            content = path.read_text(encoding='utf-8')
            version_match = re.search(r'0\.\d+\.\d+', content)
            if version_match:
                old_version = version_match.group()
                if update_file_version(path, old_version, new_version):
                    updated_count += 1
        else:
            print(f"⚠️  ファイルが見つかりません: {file_path}")
    
    print(f"\n✅ 更新完了: {updated_count}個のファイルを更新しました")
    print(f"📝 次のステップ:")
    print(f"   1. git add .")
    print(f"   2. git commit -m 'chore: bump version to {new_version}'")
    print(f"   3. git tag -a v{new_version} -m 'Release v{new_version}'")
    print(f"   4. git push && git push origin v{new_version}")

if __name__ == "__main__":
    main() 