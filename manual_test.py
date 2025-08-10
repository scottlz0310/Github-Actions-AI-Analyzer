#!/usr/bin/env python3
"""
マニュアルテストスクリプト
"""

from github_actions_ai_analyzer import GitHubActionsAnalyzer
from github_actions_ai_analyzer.types import LogLevel


def test_log_analysis():
    """ログファイルの分析をテスト"""

    # アナライザーを作成
    analyzer = GitHubActionsAnalyzer()

    # ログファイルを分析
    print("=== 基本的な失敗ログの分析 ===")
    result = analyzer.analyze_log_file(
        log_file_path="test_logs/failed_build.log",
        min_log_level=LogLevel.ERROR,
    )

    print(f"分析ID: {result.analysis_id}")
    print(f"エラー数: {len(result.error_analyses)}")
    print(f"解決策数: {len(result.solution_proposals)}")
    print(f"サマリー: {result.summary}")

    if result.error_analyses:
        print("\n=== 検出されたエラー ===")
        for i, error in enumerate(result.error_analyses, 1):
            print(f"\nエラー {i}:")
            print(f"  ID: {error.error_id}")
            print(f"  根本原因: {error.root_cause}")
            print(f"  重要度: {error.severity}")
            print(f"  影響ステップ: {error.affected_steps}")
            print(f"  関連ファイル: {error.related_files}")

    if result.solution_proposals:
        print("\n=== 提案された解決策 ===")
        for i, solution in enumerate(result.solution_proposals, 1):
            print(f"\n解決策 {i}:")
            print(f"  ID: {solution.solution_id}")
            print(f"  タイトル: {solution.title}")
            print(f"  説明: {solution.description}")
            print(f"  信頼度: {solution.confidence:.1%}")
            print(f"  推定時間: {solution.estimated_time}")

    if result.recommendations:
        print("\n=== 推奨事項 ===")
        for i, rec in enumerate(result.recommendations, 1):
            print(f"{i}. {rec}")

    print("\n" + "=" * 80)

    # 複雑な失敗ログもテスト
    print("=== 複雑な失敗ログの分析 ===")
    result2 = analyzer.analyze_log_file(
        log_file_path="test_logs/complex_failure.log",
        min_log_level=LogLevel.ERROR,
    )

    print(f"分析ID: {result2.analysis_id}")
    print(f"エラー数: {len(result2.error_analyses)}")
    print(f"解決策数: {len(result2.solution_proposals)}")
    print(f"サマリー: {result2.summary}")


if __name__ == "__main__":
    test_log_analysis()
