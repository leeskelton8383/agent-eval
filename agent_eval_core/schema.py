from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Step:
    id: int
    action: str
    tool: Optional[str]
    observation: Optional[str]

@dataclass
class AgentTrace:
    task_id: str
    question: str  # ✅ NEW FIELD
    final_answer: str
    expected_answer: str
    steps: List[Step]
    plan: Optional[List[str]] = None
    expected_tools: Optional[List[str]] = None


