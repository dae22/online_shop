import json
import sqlite3

from online_shop.domains import Product
from online_shop.schemas import AddToCart, ProductCreate, OrderCreate


class ProductRepo:
    def __init__(self, conn):
        self.conn = conn
        self.create_table()

    def create_table(self):
        query = ("""CREATE TABLE IF NOT EXISTS products (
        id PRIMARY KEY,
        name TEXT NOT NULL,
        price INTEGER NOT NULL,
        description TEXT NOT NULL
        )""")
        self.conn.execute(query)
        self.conn.commit()

    def add_product(self, product: ProductCreate) -> int:
        cur = self.conn.cursor()
        query = "INSERT INTO products (name, price, description) VALUES (?, ?, ?)"

        cur.execute(query, (product.name, product.price, product.description))
        self.conn.commit()
        return cur.lastrowid

    def get_products(self):
        self.conn.row_factory = sqlite3.Row
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM products")
        return cur.fetchall()


class CartRepo:
    def __init__(self, conn):
        self.conn = conn

    def add_to_cart(self, added_item: AddToCart):
        self.conn.execute("INSERT INTO carts VALUES (?, ?, ?)",
                          (added_item.user_id, added_item.product_id, added_item.quantity))
        self.conn.commit()
        return {"message": f"Item {added_item.product_id} added to Cart for User {added_item.user_id}"}

    def get_items(self, user_id: int):
        self.conn.row_factory = sqlite3.Row
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM carts WHERE user_id = ?", (user_id,))
        return cur.fetchall()


class OrderRepo:
    def __init__(self, conn):
        self.conn = conn

    def create_order(self, order: OrderCreate, items):
        json_items = json.dumps([dict(row) for row in items])
        cur = self.conn.cursor()
        cur.execute("INSERT INTO orders (customer_email, items) VALUES (?, ?)", (order.email, json_items))
        self.conn.commit()
        return cur.lastrowid