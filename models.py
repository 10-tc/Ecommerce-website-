import psycopg2
 
conn = psycopg2.connect(
    host="localhost",
    port=5433,
    database="e-commerce",
    user="postgres",
    password="neww"
)
 
cur = conn.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS product (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        description TEXT,
        price DECIMAL(10, 2),
        stock INT
    )
''')
cur.execute('''
    INSERT INTO product (name, description, price, stock) VALUES
    ('Product 1', 'Description for product 1', 10.00, 100),
    ('Product 2', 'Description for product 2', 20.00, 50),
    ('Product 3', 'Description for product 3', 30.00, 30)
''')
conn.commit()
cur.close()
conn.close()
 
