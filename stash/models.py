from pydantic import BaseModel, Field
from typing import List



class Company(BaseModel):
    id: int = Field(gt=0)
    company_name: str = Field(min_length=4, max_length=100)
    franchise_name: str = Field(min_length=4, max_length=100)


class Restaurant(BaseModel):
    id: int = Field(gt=0)
    company_id: int = Field(gt=0)
    terminals_amount: int = Field(gt=0) 
    restaurant_size: int = Field(gt=0)
    address: str = Field(min_length=4, max_length=100)


class RestaurantMenu(BaseModel):
    id: int = Field(gt=0)
    restaurant_id: int = Field(gt=0)
    item: str = Field(min_length=4, max_length=100)
    price: int = Field(gt=0)
    discount: int = Field(gt=0, lt=100)
    is_temporary: bool

class Order(BaseModel):
    id: int = Field(gt=0)
    restaurant_id: int = Field(gt=0)
    order_id: int = Field(gt=0)
    terminal_number: str = Field(min_length=4, max_length=100)
    items: List[str]
    to_go: bool



if __name__ == "__main__":
    a = Company(id = 1, company_name='блёва1111', franchise_name="дядя")
    print(a)