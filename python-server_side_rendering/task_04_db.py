from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

# Read JSON data
def read_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception:
        return None

# Read CSV data
def read_csv(file_path):
    products = []
    try:
        with open(file_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except Exception:
        return None

# Read SQLite data
def read_sqlite(db_path):
    products = []
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row  # Access columns by name
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            })
        conn.close()
        return products
    except Exception:
        return None

# Route for displaying products
@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id', None)
    products_data = []
    error_message = None

    # Select data source
    if source == 'json':
        file_path = os.path.join(os.path.dirname(__file__), 'products.json')
        products_data = read_json(file_path)
        if products_data is None:
            error_message = "Error reading JSON file."
    elif source == 'csv':
        file_path = os.path.join(os.path.dirname(__file__), 'products.csv')
        products_data = read_csv(file_path)
        if products_data is None:
            error_message = "Error reading CSV file."
    elif source == 'sql':
        db_path = os.path.join(os.path.dirname(__file__), 'products.db')
        products_data = read_sqlite(db_path)
        if products_data is None:
            error_message = "Error reading SQLite database."
    else:
        error_message = "Wrong source."

    # Filter by id if provided
    if products_data and product_id:
        try:
            product_id = int(product_id)
            filtered = [p for p in products_data if p.get('id') == product_id]
            if filtered:
                products_data = filtered
            else:
                error_message = "Product not found."
                products_data = []
        except ValueError:
            error_message = "Invalid id parameter."
            products_data = []

    return render_template('product_display.html', products=products_data, error=error_message)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
