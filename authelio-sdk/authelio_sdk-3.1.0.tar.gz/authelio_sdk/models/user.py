from dataclasses import dataclass
from typing import Optional, List


@dataclass
class User:
    user_id: str
    username: str
    email: str
    first_name: str
    last_name: str
    group_ids: Optional[List[str]] = None
    direct_permissions: Optional[List[str]] = None
    tmp_password: Optional[str] = None
    password: Optional[str] = None
    is_active: bool = True
    auth_type: Optional[str] = None
