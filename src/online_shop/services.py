from fastapi import HTTPException

from online_shop.repositories import ProductRepo, OrderRepo, CartRepo, UserRepo
from online_shop.resources import user_service
from online_shop.schemas import ProductCreate, AddToCart, OrderCreate, UserCreate, ProductChange


class UserService:
    def __init__(self, repo: UserRepo):
        self.repo = repo

    def add_user(self, user: UserCreate):
        return self.repo.create_user(user)

    def check_role(self, user_id: int):
        role = self.repo.check_role(user_id)
        if not role:
            raise HTTPException(status_code=404, detail="User not found")
        else:
            return role[0]


class ProductService:
    def __init__(self, repo: ProductRepo, user_service: UserService):
        self.repo = repo
        self.user_service = user_service

    def create_product(self, user_id: int, product: ProductCreate):
        role = self.user_service.check_role(user_id)
        if role == "admin":
            return self.repo.add_product(product)
        else:
            raise HTTPException(status_code=403, detail="Insufficient Rights")

    def change_product(self,user_id: int, product_id, product: ProductChange):
        role = self.user_service.check_role(user_id)
        if role != "customer":
            return self.repo.change_product(product_id, product)
        else:
            raise HTTPException(status_code=403, detail="Insufficient Rights")

    def get_products(self):
        return self.repo.get_products()


class CartService:
    def __init__(self, repo: CartRepo):
        self.repo = repo

    def add_to_cart(self, added_item: AddToCart):
        return self.repo.add_to_cart(added_item)

    def get_items(self, user_id: int):
        return self.repo.get_items(user_id)


class OrderService:
    def __init__(self, repo: OrderRepo):
        self.repo = repo

    def place_order(self, order: OrderCreate, items):
        return self.repo.create_order(order, items)
