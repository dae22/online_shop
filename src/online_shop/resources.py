from fastapi import APIRouter
import sqlite3

from online_shop.schemas import (
    ProductCreate,
    AddToCart,
    OrderCreate,
    UserCreate,
    ProductChange,
)
from online_shop.repositories import ProductRepo, OrderRepo, CartRepo, UserRepo
from online_shop.services import OrderService, ProductService, CartService, UserService
from online_shop.database import create_tables

router = APIRouter()
conn = sqlite3.connect("shop.db", check_same_thread=False)

create_tables(conn)
user_repo = UserRepo(conn)
user_service = UserService(user_repo)
product_repo = ProductRepo(conn)
product_service = ProductService(product_repo, user_service)
order_repo = OrderRepo(conn)
order_service = OrderService(order_repo)
cart_repo = CartRepo(conn)
cart_service = CartService(cart_repo)


@router.post("/product")
def create_product(user_id: int, product: ProductCreate):
    return product_service.create_product(user_id, product)


@router.patch("/product/{product_id}")
def change_product(product_id: int, user_id: int, product: ProductChange):
    return product_service.change_product(product_id, user_id, product)


@router.get("/products")
def get_products():
    return product_service.get_products()


@router.post("/cart/add")
def add_to_cart(added_item: AddToCart):
    return cart_service.add_to_cart(added_item)


@router.get("/cart/{user_id}")
def get_cart(user_id: int):
    return cart_service.get_items(user_id)


@router.post("/order")
def create_order(order: OrderCreate):
    items = cart_service.get_items(order.user_id)
    return order_service.place_order(order, items)


@router.post("/user")
def create_user(user: UserCreate):
    return user_service.add_user(user)
