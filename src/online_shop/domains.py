from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    username: str
    password: str
    role: str
    id: Optional[int] = None


@dataclass
class Product:
    name: str
    price: int
    description: str
    id: Optional[int] = None


@dataclass
class CartItem:
    product_id: int
    quantity: int = 1


@dataclass
class Order:
    email: str
    items: list[CartItem]
