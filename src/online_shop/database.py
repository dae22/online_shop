def create_tables(conn):
    create_products = """CREATE TABLE IF NOT EXISTS products (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       price INTEGER NOT NULL,
                       description TEXT NOT NULL
                       )"""
    create_carts = """CREATE TABLE IF NOT EXISTS carts (
                    user_id INTEGER NOT NULL,
                    product_id INTEGER NOT NULL,
                    quantity INTEGER NOT NULL,
                    FOREIGN KEY (product_id) REFERENCES products(id),
                    FOREIGN KEY (user_id) REFERENCES users(id)
                    )"""
    create_orders = """CREATE TABLE IF NOT EXISTS orders (
                        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        customer_email TEXT NOT NULL,
                        items TEXT NOT NULL
                        )"""
    create_users = """CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL,
                        role TEXT NOT NULL
                        )"""
    conn.execute(create_users)
    conn.execute(create_products)
    conn.execute(create_carts)
    conn.execute(create_orders)
