from flask import Flask, render_template, request, redirect, url_for, session
import psycopg2
 
app = Flask(__name__)
app.secret_key = 'your_secret_key'
 
# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        port=5433,
        database="e-commerce",
        user="postgres",
        password="neww"
    )
    return conn
 
@app.route('/')
def index():
    print("Index route accessed")
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM product')
    product = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', product=product)
 
@app.route('/product/<int:product_id>')
def product(product_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM product WHERE id = %s', (product_id,))
    product = cur.fetchone()
    cur.close()
    conn.close()
    return render_template('product.html', product=product)
 
@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(product_id)
    print(f"Product {product_id} added to cart. Current cart: {session['cart']}")
    return redirect(url_for('cart'))
 
@app.route('/cart')
def cart():
    if 'cart' not in session:
        return render_template('cart.html', product=[])
   
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM product WHERE id IN %s', (tuple(session['cart']),))
    product = cur.fetchall()
    print(f"Products in cart: {product}")
    cur.close()
    conn.close()
    return render_template('cart.html', product=product)
 
@app.route('/search')
def search():
    # Your search logic here
    return "Search page"
 
if __name__ == '__main__':
    app.run(debug=True)
 
has context menu
