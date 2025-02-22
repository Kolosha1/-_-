import sqlite3

class DBManager():
    def __init__(self,dbname):
        self.dbname = dbname
        self.conn = None
        self.cursor = None

    def open_db(self):
        self.conn =sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()

    def get_categories(self):
        self.open_db()
        self.cursor.execute('''SELECT * FROM categories''')
        data = self.cursor.fetchall()
        self.conn.close()
        return data
    
    def get_meals(self):
        self.open_db()
        self.cursor.execute('''SELECT * FROM meals''')
        data = self.cursor.fetchall()
        self.conn.close()
        return data
    def get_meals_by_category(self,category_id):
        self.open_db()
        self.cursor.execute('''SELECT * FROM meals WHERE category_id=?''',[category_id]) 
        data = self.cursor.fetchall()
        self.conn.close()
        return data
    def get_meals_by_id(self,meals_id):
        self.open_db()
        self.cursor.execute('''SELECT * FROM meals WHERE id=?''',[meals_id]) 
        data = self.cursor.fetchone()
        self.conn.close()
        return data
    
    def create_order(self,title,description,text,image,autor_id,category_id):
        self.open_db()
        self.cursor.execute('''INSERT INTO articles(title,description,text,image,author_id,category_id) VALUES(?,?,?,?,?,?)''',[title,description,text,image,autor_id,category_id])
        self.conn.commit()
        self.conn.close()

    def search_meals(self,query):
        self.open_db()
        query ='%' + query + '%'
        self.cursor.execute('''SELECT * FROM meals WHERE (title LIKE? OR description LIKE?)''',[query,query]) 
        data = self.cursor.fetchall()
        self.conn.close()
        return data