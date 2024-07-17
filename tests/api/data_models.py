from dataclasses import dataclass
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class UserDetails:
    first_name: str
    last_name : str
    email: str
    password: Optional[str] = field(default=None)
    id: Optional[str] = field(default=None)

@dataclass
class ApiCredentials:
    auth_token : str


# Exceptions
class AuthenticationError(Exception):
    pass

class GetUserError(Exception):
    pass

class CreateUserError(Exception):
    pass

class UpdateUserError(Exception):
    pass
