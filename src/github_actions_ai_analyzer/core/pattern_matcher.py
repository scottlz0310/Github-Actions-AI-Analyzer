"""
パターンマッチャー

エラーパターンとのマッチングを行い、構造化されたエラー情報を抽出します。
"""

import re
from typing import List

from ..types import ErrorPattern, LogEntry, PatternCategory, PatternMatch


class PatternMatcher:
    """エラーパターンマッチングを行うクラス"""

    def __init__(self):
        self.patterns: List[ErrorPattern] = []
        self._load_default_patterns()

    def _load_default_patterns(self) -> None:
        """デフォルトのエラーパターンを読み込み"""
        # 依存関係エラー
        self.patterns.extend(
            [
                ErrorPattern(
                    id="dep_missing_package",
                    name="Missing Package",
                    category=PatternCategory.DEPENDENCY,
                    regex_pattern=r"ModuleNotFoundError: No module named '([^']+)'",
                    description="Pythonパッケージが見つからない",
                    severity="error",
                    language="python",
                ),
                ErrorPattern(
                    id="dep_version_conflict",
                    name="Version Conflict",
                    category=PatternCategory.DEPENDENCY,
                    regex_pattern=r"ERROR: Cannot uninstall '([^']+)'.*version conflict",
                    description="パッケージのバージョン競合",
                    severity="error",
                    language="python",
                ),
                ErrorPattern(
                    id="npm_install_failed",
                    name="npm Install Failed",
                    category=PatternCategory.DEPENDENCY,
                    regex_pattern=r"npm ERR!.*install",
                    description="npm installの失敗",
                    severity="error",
                    language="javascript",
                ),
            ]
        )

        # 権限エラー
        self.patterns.extend(
            [
                ErrorPattern(
                    id="perm_denied",
                    name="Permission Denied",
                    category=PatternCategory.PERMISSION,
                    regex_pattern=r"Permission denied|EACCES|EACCESS",
                    description="ファイルアクセス権限エラー",
                    severity="error",
                ),
                ErrorPattern(
                    id="perm_execute",
                    name="Execute Permission",
                    category=PatternCategory.PERMISSION,
                    regex_pattern=r"Permission denied.*executable",
                    description="実行権限エラー",
                    severity="error",
                ),
            ]
        )

        # 環境エラー
        self.patterns.extend(
            [
                ErrorPattern(
                    id="env_command_not_found",
                    name="Command Not Found",
                    category=PatternCategory.ENVIRONMENT,
                    regex_pattern=r"command not found|No such file or directory",
                    description="コマンドが見つからない",
                    severity="error",
                ),
                ErrorPattern(
                    id="env_python_version",
                    name="Python Version Mismatch",
                    category=PatternCategory.ENVIRONMENT,
                    regex_pattern=r"Python.*version.*required",
                    description="Pythonバージョンの不一致",
                    severity="error",
                    language="python",
                ),
            ]
        )

        # ネットワークエラー
        self.patterns.extend(
            [
                ErrorPattern(
                    id="net_timeout",
                    name="Network Timeout",
                    category=PatternCategory.NETWORK,
                    regex_pattern=r"timeout|TIMEOUT|Connection timed out",
                    description="ネットワークタイムアウト",
                    severity="error",
                ),
                ErrorPattern(
                    id="net_connection_refused",
                    name="Connection Refused",
                    category=PatternCategory.NETWORK,
                    regex_pattern=r"Connection refused|ECONNREFUSED",
                    description="接続が拒否された",
                    severity="error",
                ),
            ]
        )

        # 構文エラー
        self.patterns.extend(
            [
                ErrorPattern(
                    id="syntax_yaml",
                    name="YAML Syntax Error",
                    category=PatternCategory.SYNTAX,
                    regex_pattern=r"YAML.*syntax error|yaml.*error",
                    description="YAML構文エラー",
                    severity="error",
                ),
                ErrorPattern(
                    id="syntax_json",
                    name="JSON Syntax Error",
                    category=PatternCategory.SYNTAX,
                    regex_pattern=r"JSON.*syntax error|json.*error",
                    description="JSON構文エラー",
                    severity="error",
                ),
            ]
        )

    def match_patterns(
        self, log_entries: List[LogEntry]
    ) -> List[PatternMatch]:
        """ログエントリに対してパターンマッチングを実行"""
        matches = []

        for entry in log_entries:
            entry_matches = self._match_entry(entry)
            matches.extend(entry_matches)

        return matches

    def _match_entry(self, entry: LogEntry) -> List[PatternMatch]:
        """単一のログエントリに対してパターンマッチングを実行"""
        matches = []

        for pattern in self.patterns:
            # 言語フィルタリング
            if (
                pattern.language
                and entry.metadata.get("language") != pattern.language
            ):
                continue

            # 正規表現マッチング
            regex = re.compile(pattern.regex_pattern, re.IGNORECASE)
            match = regex.search(entry.message)

            if match:
                confidence = self._calculate_confidence(pattern, entry, match)
                if confidence > 0.5:  # 信頼度が50%以上の場合のみ
                    pattern_match = PatternMatch(
                        pattern=pattern,
                        matched_text=match.group(0),
                        start_pos=match.start(),
                        end_pos=match.end(),
                        confidence=confidence,
                        context={
                            "log_entry": entry,
                            "match_groups": match.groups(),
                            "full_message": entry.message,
                        },
                    )
                    matches.append(pattern_match)

        return matches

    def _calculate_confidence(
        self, pattern: ErrorPattern, entry: LogEntry, match: re.Match
    ) -> float:
        """マッチングの信頼度を計算"""
        confidence = 0.5  # ベース信頼度

        # ログレベルによる調整
        if entry.level == "error" and pattern.severity == "error":
            confidence += 0.2
        elif entry.level == "warning" and pattern.severity == "warning":
            confidence += 0.1

        # 完全一致による調整
        if match.group(0) == entry.message:
            confidence += 0.2

        # パターンの詳細度による調整
        if len(pattern.regex_pattern) > 50:
            confidence += 0.1

        return min(confidence, 1.0)

    def add_pattern(self, pattern: ErrorPattern) -> None:
        """新しいパターンを追加"""
        self.patterns.append(pattern)

    def get_patterns_by_category(
        self, category: PatternCategory
    ) -> List[ErrorPattern]:
        """カテゴリ別にパターンを取得"""
        return [p for p in self.patterns if p.category == category]

    def get_patterns_by_language(self, language: str) -> List[ErrorPattern]:
        """言語別にパターンを取得"""
        return [p for p in self.patterns if p.language == language]

    def remove_pattern(self, pattern_id: str) -> bool:
        """パターンを削除"""
        for i, pattern in enumerate(self.patterns):
            if pattern.id == pattern_id:
                del self.patterns[i]
                return True
        return False
