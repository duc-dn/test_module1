from pydatic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    is_active: bool = True