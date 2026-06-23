from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

# Function to read JSON file
def read_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None

# Function to read CSV file
def read_csv(file_path):
    products = []
    try:
        with open(file_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert numeric fields
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except FileNotFoundError:
        return None
    except Exception:
        return None

# Route to display products
@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id', None)
    products_data = []
    error_message = None

    # Determine source and read data
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
