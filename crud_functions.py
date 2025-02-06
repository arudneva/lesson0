import sqlite3

def initiate_db():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Prod(
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                price INTEGER NOT NULL
            )
        ''')
    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Prod')
    products = cursor.fetchall()
    connection.close()
    return products

initiate_db()

connection = sqlite3.connect('products.db')
cursor = connection.cursor()

if not get_all_products():
    products = [
        ('Продукт1', 'Описание продукта 1', 100),
        ('Продукт2', 'Описание продукта 2', 200),
        ('Продукт3', 'Описание продукта 3', 300),
        ('Продукт4', 'Описание продукта 4', 400)
    ]

    cursor.executemany('INSERT INTO Prod (title, description, price) VALUES (?, ?, ?)', products)
    connection.commit()

connection.close()