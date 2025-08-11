from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    price: int
    description: str


class ProductChange(BaseModel):
    price: int
    description: str


class UserResponse(BaseModel):
    id: int
    username: str


class AddToCart(BaseModel):
    user_id: int
    product_id: int
    quantity: int


class OrderCreate(BaseModel):
    email: str
    user_id: int


class UserCreate(BaseModel):
    username: str
    password: str
    role: str = "customer"
