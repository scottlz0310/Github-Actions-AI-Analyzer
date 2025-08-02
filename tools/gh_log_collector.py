#!/usr/bin/env python3
"""
GitHub Actions ログ収集とAI解析の自動化スクリプト

使用方法:
    python tools/gh_log_collector.py
    
機能:
- gh run list でワークフロー実行一覧を取得
- インタラクティブに実行を選択
- ログを logs/ ディレクトリに保存
- AI解析ツールで自動解析
"""

import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional


class GitHubActionsLogCollector:
    def __init__(self):
        self.logs_dir = Path("logs")
        self.logs_dir.mkdir(exist_ok=True)
        
    def check_gh_cli(self) -> bool:
        """GitHub CLI (gh) が利用可能かチェック"""
        try:
            result = subprocess.run(
                ["gh", "--version"], 
                capture_output=True, 
                text=True, 
                check=True
            )
            print(f"✅ GitHub CLI 利用可能: {result.stdout.strip()}")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("❌ GitHub CLI (gh) が見つかりません")
            print("インストール方法: https://cli.github.com/")
            return False

    def get_workflow_runs(self, limit: int = 10) -> List[Dict]:
        """ワークフロー実行一覧を取得"""
        try:
            result = subprocess.run(
                ["gh", "run", "list", "--limit", str(limit), "--json", 
                 "databaseId,displayTitle,status,conclusion,workflowName,createdAt"],
                capture_output=True,
                text=True,
                check=True
            )
            return json.loads(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"❌ ワークフロー実行一覧の取得に失敗: {e}")
            return []

    def display_runs(self, runs: List[Dict]) -> None:
        """ワークフロー実行一覧を表示"""
        print("\n📋 GitHub Actions ワークフロー実行一覧:")
        print("-" * 80)
        print(f"{'#':<3} {'ID':<10} {'ステータス':<10} {'ワークフロー':<25} {'作成日時':<20}")
        print("-" * 80)
        
        for i, run in enumerate(runs, 1):
            status_icon = self._get_status_icon(run["status"], run["conclusion"])
            created_at = datetime.fromisoformat(
                run["createdAt"].replace("Z", "+00:00")
            ).strftime("%m/%d %H:%M")
            
            workflow_name = run["workflowName"][:23] + "..." if len(run["workflowName"]) > 25 else run["workflowName"]
            
            print(f"{i:<3} {run['databaseId']:<10} {status_icon:<10} {workflow_name:<25} {created_at:<20}")

    def _get_status_icon(self, status: str, conclusion: Optional[str]) -> str:
        """ステータスアイコンを取得"""
        if status == "completed":
            if conclusion == "success":
                return "✅ success"
            elif conclusion == "failure":
                return "❌ failure"
            elif conclusion == "cancelled":
                return "⏹️ cancelled"
            else:
                return f"❓ {conclusion}"
        elif status == "in_progress":
            return "🔄 running"
        else:
            return f"⏸️ {status}"

    def select_run(self, runs: List[Dict]) -> Optional[Dict]:
        """ユーザーにワークフロー実行を選択させる"""
        while True:
            try:
                choice = input(f"\n選択してください (1-{len(runs)}, q=終了): ").strip()
                if choice.lower() == 'q':
                    return None
                
                index = int(choice) - 1
                if 0 <= index < len(runs):
                    return runs[index]
                else:
                    print(f"❌ 1から{len(runs)}の範囲で入力してください")
            except ValueError:
                print("❌ 数字を入力してください")

    def download_log(self, run: Dict) -> Optional[str]:
        """指定されたワークフロー実行のログをダウンロード"""
        run_id = run["databaseId"]
        workflow_name = run["workflowName"]
        status = run["status"]
        conclusion = run.get("conclusion", "unknown")
        
        # ファイル名を生成（安全な文字のみ使用）
        safe_workflow_name = "".join(
            c for c in workflow_name if c.isalnum() or c in ('-', '_', ' ')
        ).replace(' ', '_')
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{safe_workflow_name}_{run_id}_{status}_{conclusion}_{timestamp}.log"
        filepath = self.logs_dir / filename
        
        print(f"\n📥 ログをダウンロード中: {run['displayTitle']}")
        print(f"💾 保存先: {filepath}")
        
        try:
            result = subprocess.run(
                ["gh", "run", "view", str(run_id), "--log"],
                capture_output=True,
                text=True,
                check=True
            )
            
            # ログをファイルに保存
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"# GitHub Actions ワークフロー実行ログ\n")
                f.write(f"# ワークフロー: {workflow_name}\n")
                f.write(f"# 実行ID: {run_id}\n")
                f.write(f"# ステータス: {status} ({conclusion})\n")
                f.write(f"# 作成日時: {run['createdAt']}\n")
                f.write(f"# ダウンロード日時: {datetime.now().isoformat()}\n")
                f.write("# " + "=" * 70 + "\n\n")
                f.write(result.stdout)
            
            print(f"✅ ログ保存完了: {filepath}")
            return str(filepath)
            
        except subprocess.CalledProcessError as e:
            print(f"❌ ログダウンロードに失敗: {e}")
            return None

    def run_ai_analysis(self, log_file: str) -> None:
        """AI解析ツールでログを解析"""
        print(f"\n🤖 AI解析を実行中: {log_file}")
        
        # AI解析ツール（enhanced版）のパス
        analyzer_path = "tools/github_actions_ai_analyzer_enhanced.py"
        
        if not os.path.exists(analyzer_path):
            print(f"❌ AI解析ツールが見つかりません: {analyzer_path}")
            return
            
        try:
            # AI解析ツールを実行（ログファイルのみを解析）
            result = subprocess.run(
                [sys.executable, analyzer_path, log_file],
                capture_output=True,
                text=True,
                check=True
            )
            
            print("✅ AI解析完了")
            print("\n📊 解析結果:")
            print("-" * 50)
            print(result.stdout)
            
        except subprocess.CalledProcessError as e:
            print(f"❌ AI解析に失敗: {e}")
            if e.stdout:
                print(f"stdout: {e.stdout}")
            if e.stderr:
                print(f"stderr: {e.stderr}")

    def interactive_menu(self) -> None:
        """メインのインタラクティブメニュー"""
        print("🚀 GitHub Actions ログ収集 & AI解析ツール")
        print("=" * 50)
        
        while True:
            print("\n📋 メニュー:")
            print("1. ワークフロー実行一覧を表示してログ収集")
            print("2. 既存ログファイルをAI解析")
            print("3. logs/ ディレクトリの内容を表示")
            print("q. 終了")
            
            choice = input("\n選択してください: ").strip()
            
            if choice == "1":
                self.collect_and_analyze_logs()
            elif choice == "2":
                self.analyze_existing_logs()
            elif choice == "3":
                self.show_logs_directory()
            elif choice.lower() == "q":
                print("👋 終了します")
                break
            else:
                print("❌ 無効な選択です")

    def collect_and_analyze_logs(self) -> None:
        """ログ収集とAI解析を実行"""
        # ワークフロー実行数を選択
        while True:
            try:
                limit = input("\n表示する実行数を入力 (デフォルト: 10): ").strip()
                limit = int(limit) if limit else 10
                if limit > 0:
                    break
                else:
                    print("❌ 正の数を入力してください")
            except ValueError:
                print("❌ 数字を入力してください")

        # ワークフロー実行一覧を取得
        runs = self.get_workflow_runs(limit)
        if not runs:
            print("❌ ワークフロー実行が見つかりません")
            return

        # 実行一覧を表示
        self.display_runs(runs)

        # ユーザーに選択させる
        selected_run = self.select_run(runs)
        if not selected_run:
            return

        # ログをダウンロード
        log_file = self.download_log(selected_run)
        if not log_file:
            return

        # AI解析を実行するか確認
        analyze = input("\n🤖 AI解析を実行しますか? (y/N): ").strip().lower()
        if analyze in ('y', 'yes'):
            self.run_ai_analysis(log_file)

    def analyze_existing_logs(self) -> None:
        """既存のログファイルをAI解析"""
        log_files = list(self.logs_dir.glob("*.log"))
        if not log_files:
            print("❌ logs/ ディレクトリにログファイルがありません")
            return

        print("\n📁 既存ログファイル:")
        print("-" * 50)
        for i, log_file in enumerate(log_files, 1):
            file_size = log_file.stat().st_size / 1024  # KB
            modified_time = datetime.fromtimestamp(
                log_file.stat().st_mtime
            ).strftime("%m/%d %H:%M")
            print(f"{i:<3} {log_file.name:<40} {file_size:>8.1f}KB {modified_time}")

        # ファイルを選択
        while True:
            try:
                choice = input(f"\n解析するファイルを選択 (1-{len(log_files)}, q=戻る): ").strip()
                if choice.lower() == 'q':
                    return
                
                index = int(choice) - 1
                if 0 <= index < len(log_files):
                    selected_file = log_files[index]
                    self.run_ai_analysis(str(selected_file))
                    break
                else:
                    print(f"❌ 1から{len(log_files)}の範囲で入力してください")
            except ValueError:
                print("❌ 数字を入力してください")

    def show_logs_directory(self) -> None:
        """logs/ ディレクトリの内容を表示"""
        log_files = list(self.logs_dir.glob("*"))
        if not log_files:
            print("❌ logs/ ディレクトリは空です")
            return

        print(f"\n📁 {self.logs_dir}/ ディレクトリの内容:")
        print("-" * 80)
        print(f"{'ファイル名':<50} {'サイズ':<10} {'更新日時':<20}")
        print("-" * 80)
        
        for log_file in sorted(log_files, key=lambda x: x.stat().st_mtime, reverse=True):
            if log_file.is_file():
                file_size = log_file.stat().st_size / 1024  # KB
                modified_time = datetime.fromtimestamp(
                    log_file.stat().st_mtime
                ).strftime("%Y/%m/%d %H:%M")
                print(f"{log_file.name:<50} {file_size:>8.1f}KB {modified_time:<20}")

    def run(self) -> None:
        """メインエントリーポイント"""
        if not self.check_gh_cli():
            return
            
        self.interactive_menu()


def main():
    """メイン関数"""
    collector = GitHubActionsLogCollector()
    collector.run()


if __name__ == "__main__":
    main()