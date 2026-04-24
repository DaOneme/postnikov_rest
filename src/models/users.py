from pydantic import BaseModel, EmailStr, Field
from pydantic_extra_types.phone_numbers import PhoneNumber
from pydantic_extra_types.payment import PaymentCardNumber
from typing import Optional


PhoneNumber.phone_format = 'E164'

class UserAdd(BaseModel):
    name: str = Field(min_length=2, max_length=30)
    surname: str = Field(min_length=2, max_length=30)
    phone: Optional[PhoneNumber] = None
    email: EmailStr
    address: Optional[str] = Field(default=None, max_length=100)
    payment: Optional[PaymentCardNumber] = None

class User(UserAdd):
    id: int


if __name__ == "__main__":
    a = UserAdd(
        name="Alex", 
        surname="Grob", 
        phone="+79965159063",
        email="alex@example.com")
    
    print(a)