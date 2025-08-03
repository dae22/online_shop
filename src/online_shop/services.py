from online_shop.repositories import ProductRepo, OrderRepo, CartRepo
from online_shop.schemas import ProductCreate, AddToCart, OrderCreate


class ProductService:
    def __init__(self, repo: ProductRepo):
        self.repo = repo

    def create_product(self, product: ProductCreate) -> int:
        return self.repo.add_product(product)

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
