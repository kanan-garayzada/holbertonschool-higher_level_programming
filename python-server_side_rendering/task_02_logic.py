from flask import Flask, render_template
import json
import os

app = Flask(__name__)

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route for items page
@app.route('/items')
def items():
    items_list = []

    # Read items from JSON file
    json_path = os.path.join(os.path.dirname(__file__), 'items.json')
    try:
        with open(json_path, 'r') as f:
            data = json.load(f)
            items_list = data.get("items", [])
    except FileNotFoundError:
        print("items.json file not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON file.")

    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
