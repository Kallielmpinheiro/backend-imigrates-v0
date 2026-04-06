from ninja import Schema

class LoginSchema(Schema):
    email: str
    password: str

class TokenSchema(Schema):
    access: str
    refresh: str

class RefreshSchema(Schema):
    refresh: str