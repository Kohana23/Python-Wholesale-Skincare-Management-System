# read.py

def load_products(PRODUCT_FILE):
    products = {}
    try:
        with open(PRODUCT_FILE, "r") as file:
            for line in file:
                clean_line = line.replace(' ,', ',').replace(', ', ',').replace('\n', '')
                try:
                    name, brand, quantity, cost_price, country = clean_line.split(',')
                    products[name] = {
                        'brand': brand,
                        'stock': int(quantity),
                        'cost': float(cost_price),
                        'selling_price': round(float(cost_price) * 2),
                        'country': country
                    }
                except ValueError:
                    print("Error parsing line (should have 5 values): " + line)
                    continue
    except FileNotFoundError:
        print("Product file not found. Creating a new one.")
        open(PRODUCT_FILE, "w")
        
    return products
