from pydantic import BaseModel, EmailStr, Field

class UserSchema(BaseModel):
    name: str = Field(min_length = 3, max_length = 20)
    email: EmailStr
