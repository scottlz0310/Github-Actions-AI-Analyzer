"""
ログ関連の型定義

GitHub Actionsのログエントリとログレベルを定義します。
"""

from enum import Enum
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime


class LogLevel(str, Enum):
    """ログレベル"""
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    FATAL = "fatal"


class LogSource(str, Enum):
    """ログの発生源"""
    WORKFLOW = "workflow"
    STEP = "step"
    ACTION = "action"
    SYSTEM = "system"
    USER = "user"


class LogEntry(BaseModel):
    """ログエントリ"""
    timestamp: datetime = Field(..., description="ログのタイムスタンプ")
    level: LogLevel = Field(..., description="ログレベル")
    source: LogSource = Field(..., description="ログの発生源")
    message: str = Field(..., description="ログメッセージ")
    step_name: Optional[str] = Field(None, description="ステップ名")
    action_name: Optional[str] = Field(None, description="アクション名")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="追加メタデータ")
    
    class Config:
        use_enum_values = True 