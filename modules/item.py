from db import CURSOR, CONN


class Item:
    def __init__(self, id, name, quantity, price, category, location):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category
        self.location = location

    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                quantity INTEGER,
                price REAL,
                category TEXT,
                location TEXT
            );
        """)
        CONN.commit()

    @classmethod
    def create(cls, name, quantity, price, category, location):
        CURSOR.execute("""
            INSERT INTO items (name, quantity, price, category, location)
            VALUES (?, ?, ?, ?, ?);
        """, (name, quantity, price, category, location))
        CONN.commit()

    @classmethod
    def get_all(cls):
        rows = CURSOR.execute("SELECT * FROM items").fetchall()
        return [cls(*row) for row in rows]

    @classmethod
    def find_by_id(cls, item_id):
        row = CURSOR.execute("SELECT * FROM items WHERE id=?", (item_id,)).fetchone()
        return cls(*row) if row else None

    @classmethod
    def find_by_name(cls, name):
        rows = CURSOR.execute("SELECT * FROM items WHERE name LIKE ?", ('%' + name + '%',)).fetchall()
        return [cls(*row) for row in rows]

    @classmethod
    def find_by_category(cls, category):
        rows = CURSOR.execute("SELECT * FROM items WHERE category LIKE ?", ('%' + category + '%',)).fetchall()
        return [cls(*row) for row in rows]

    def update(self):
        CURSOR.execute("""
            UPDATE items
            SET name=?, quantity=?, price=?, category=?, location=?
            WHERE id=?;
        """, (self.name, self.quantity, self.price, self.category, self.location, self.id))
        CONN.commit()

    def delete(self):
        CURSOR.execute("DELETE FROM items WHERE id=?", (self.id,))
        CONN.commit()
