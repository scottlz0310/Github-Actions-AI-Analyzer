"""
型定義パッケージ

GitHub Actions AI Analyzerで使用する型定義を提供します。
"""

from .log_types import LogEntry, LogLevel, LogSource
from .context_types import RepositoryContext, WorkflowContext, EnvironmentContext
from .pattern_types import ErrorPattern, PatternMatch, PatternCategory
from .analysis_types import AnalysisResult, ErrorAnalysis, SolutionProposal

__all__ = [
    # log_types
    "LogEntry",
    "LogLevel",
    "LogSource",
    
    # context_types
    "RepositoryContext",
    "WorkflowContext",
    "EnvironmentContext",
    
    # pattern_types
    "ErrorPattern",
    "PatternMatch",
    "PatternCategory",
    
    # analysis_types
    "AnalysisResult",
    "ErrorAnalysis",
    "SolutionProposal",
] 