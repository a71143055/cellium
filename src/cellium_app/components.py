from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class Component:
    id: str
    type: str
    params: Dict[str, Any] = field(default_factory=dict)
