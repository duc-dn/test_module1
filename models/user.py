from pydatic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str