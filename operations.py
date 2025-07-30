def display_products(products):
    print("\nAvailable Products in Stock:")
    print("------------------------------------------------------------------------")
    print("ID   Product Name           Brand               Qty  Price    Country")
    print("------------------------------------------------------------------------")

    i = 1
    for name, details in products.items():
        id_str = str(i)
        while len(id_str) < 4:
            id_str += " "
        
        name_str = name
        while len(name_str) < 22:
            name_str += " "
        
        brand_str = details['brand']
        while len(brand_str) < 20:
            brand_str += " "
        
        qty_str = str(details['stock'])
        while len(qty_str) < 5:
            qty_str += " "
        
        price_str = "Rs" + str(details['selling_price'])
        while len(price_str) < 7:
            price_str += " "
        
        print(id_str + name_str + brand_str + qty_str + price_str + details['country'])
        i += 1

def process_sale(products):
    customer_name = input("Enter customer name: ")
    total_invoice_lines = []
    grand_total = 0

    while True:
        product_list = list(products.items())
        print("\nAvailable Products in Stock:")
        print("------------------------------------------------------------------------")
        print("ID   Product Name           Brand               Qty  Price    Country")
        print("------------------------------------------------------------------------")

        id_to_product = {}
        i = 1
        for item in product_list:
            name, details = item
            id_str = str(i)
            while len(id_str) < 4:
                id_str += " "
            
            name_str = name
            while len(name_str) < 22:
                name_str += " "
            
            brand_str = details['brand']
            while len(brand_str) < 20:
                brand_str += " "
            
            qty_str = str(details['stock'])
            while len(qty_str) < 5:
                qty_str += " "
            
            price_str = "Rs" + str(details['selling_price'])
            while len(price_str) < 7:
                price_str += " "
            
            print(id_str + name_str + brand_str + qty_str + price_str + details['country'])
            id_to_product[i] = (name, details)
            i += 1

        try:
            product_id = int(input("Enter product ID to purchase: "))
            if product_id not in id_to_product:
                print("Invalid product ID.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        product_name, product_info = id_to_product[product_id]

        try:
            quantity = int(input("Enter quantity to purchase: "))
        except ValueError:
            print("Invalid quantity.")
            continue

        stock = product_info["stock"]
        if quantity > stock:
            print("Not enough stock available.")
            continue

        free_items = quantity // 3
        total_quantity = quantity + free_items
        if total_quantity > stock:
            print("Not enough stock to provide free items. Sale cannot be completed.")
            continue

        cost = quantity * product_info["selling_price"]
        grand_total += cost

        product_info["stock"] -= total_quantity

        invoice_line = "Product: " + product_name + " | Brand: " + product_info['brand'] + " | Bought: " + str(quantity) + " | Free: " + str(free_items) + " | Subtotal: Rs " + str(cost)
        total_invoice_lines.append(invoice_line)

        more = input("Do you want to buy another product? (yes/no): ").lower()
        if more != 'yes':
            break

    if total_invoice_lines:
        vat = round(grand_total * 0.15, 2)
        amount_to_pay = round(grand_total + vat, 2)
        return customer_name, total_invoice_lines, grand_total, vat, amount_to_pay
    else:
        print("No items purchased.")
        return None, [], 0, 0, 0

def restock_products(products):
    supplier = input("Enter supplier name: ")
    items_bought = []
    total_amount = 0

    while True:
        print("\nOptions:")
        print("1. Restock existing product")
        print("2. Add new product")
        print("3. Finish restocking")
        choice = input("Enter your choice (1-3): ")

        if choice == "3":
            break

        if choice == "1":  # Restock existing product
            if not products:
                print("No products available to restock. Please add new products first.")
                continue

            display_products(products)
            try:
                product_id = int(input("Enter product ID to restock: "))
                product_list = list(products.items())
                if product_id < 1 or product_id > len(product_list):
                    print("Invalid product ID.")
                    continue
            except ValueError:
                print("Please enter a valid number.")
                continue

            product_name, product_details = product_list[product_id - 1]
            
            print("\nExisting product details:")
            print("Name: " + product_name)
            print("Brand: " + product_details['brand'])
            print("Current stock: " + str(product_details['stock']))
            print("Current cost: " + str(product_details['cost']))
            print("Current selling price: " + str(product_details['selling_price']))
            print("Country: " + product_details['country'])

            # Ask if user wants to change cost price
            change_cost = input("Do you want to change the cost price? (yes/no): ").lower()
            if change_cost == 'yes':
                try:
                    new_cost = float(input("Enter new cost per unit: "))
                    product_details['cost'] = new_cost
                    product_details['selling_price'] = round(new_cost * 2)
                except ValueError:
                    print("Invalid number. Keeping previous cost price.")

            # Get quantity to add
            try:
                qty = int(input("Enter quantity to add: "))
            except ValueError:
                print("Invalid quantity. Try again.")
                continue

            # Update stock
            product_details['stock'] += qty

            # Calculate total and add to items bought
            item_total = qty * product_details['cost']
            total_amount += item_total
            items_bought.append({
                'Product': product_name,
                'Brand': product_details['brand'],
                'Qty': qty,
                'Rate': product_details['cost'],
                'Total': item_total
            })

            print("\nAdded " + str(qty) + " units of " + product_name + ". New stock: " + str(product_details['stock']) + "\n")

        elif choice == "2":  # Add new product
            name = input("Enter new product name: ")
            brand = input("Enter brand: ")
            try:
                qty = int(input("Enter initial quantity: "))
                rate = float(input("Enter cost per unit: "))
            except ValueError:
                print("Invalid number. Try again.")
                continue
            country = input("Enter country of origin: ")

            # Add new product to dictionary
            products[name] = {
                'brand': brand,
                'stock': qty,
                'cost': rate,
                'selling_price': round(rate * 2),
                'country': country
            }

            item_total = qty * rate
            total_amount += item_total
            items_bought.append({
                'Product': name,
                'Brand': brand,
                'Qty': qty,
                'Rate': rate,
                'Total': item_total
            })

            print("\nAdded new product: " + name + " (" + brand + ")\n")

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    return supplier, items_bought, total_amount
