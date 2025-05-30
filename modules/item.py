from lib import CONN, CURSOR

class Item:
    all = {}

    def __init__(self, name, quantity, price, category = None, id = None):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category 

    def __repr__(self):
        return f"<Item: {id}: name: {self.name}, Qty: {self.quantity}, " + f"<Price: ${self.price:.2f}, Category: {self.category}, " 
    
    @classmethod
    def create_table(cls):
        sql = """
           CREATE TABLE IF NOT EXISTS items (
              id INTEGER PRIMARY KEY, 
              name TEXT NOT NULL,
              quantity INTEGER NOT NULL,
              price REAL NOT NULL,
              category TEXT
           )               
        """

        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def drop_table(cls):
        sql = """
           DROP TABLE IF EXISTS items 
        """    

        CURSOR.execute(sql)
        CONN.commit()
        cls.all = {} 

    def save(self):
       sql = """
           INSERT INTO items(name, quantity, price, category)
           VALUES (?,?,?,?)            
        """ 
       
       CURSOR.execute(sql, (self.name, self.quantity, self.price, self.category))
       CONN.commit()

       self.id = CURSOR.lastrowid
       type(self).all[self.id] = self

    def update(self):
        sql = """
           UPDATE items
           SET name = ?, quantity = ?, price = ?, category = ?
           WHERE id = ?
        """   
        CURSOR.execute(sql, (self.name, self.quantity, self.price, self.category))
        CONN.commit()

    def delete(self):
        sql = """
           DELETE items
           WHERE id = ?
        """    

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id] 
        self.id = None

    @classmethod
    def create_table(cls, name, quantity, price, category = None):
        item = cls(name, quantity, price, category)
        item.save()
        return item   

    @classmethod 
    def instance_from_db(cls,row):
        item = cls.all.get(row[0])

        if item:
            item.name = row[1]
            item.quantity = row[2]
            item.price = row[3]
            item.category = row[4]

        else:
            item = cls(row[1], row[2], row[3], row[4], row[0])   
            cls.all[item.id] = item 
        return item

    @classmethod
    def get_all(cls):
        sql = """
           SELECT *
           FROM items
        """    

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
           SELECT *
           FROM items
           WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None 
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
           SELECT *
           FROM items
           WHERE name = ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_category(cls, category):
        sql = """
           SELECT *
           FROM items
           WHERE category = ?
        """

        row = CURSOR.execute(sql, (category,)).fetchone()
        return cls.instance_from_db(row) if row else None
     
        

