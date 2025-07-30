# write.py
import datetime

def save_products(PRODUCT_FILE, products):
    with open(PRODUCT_FILE, 'w') as file:
        for name, details in products.items():
            file.write(name + "," + details['brand'] + "," + str(details['stock']) + "," + str(details['cost']) + "," + details['country'] + "\n")

def generate_invoice(customer_name, total_invoice_lines, grand_total, vat, amount_to_pay):
    now = datetime.datetime.now()
    invoice_name = "invoice_" + customer_name + "_" + str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second) + ".txt"
    
    with open(invoice_name, "w") as file:
        file.write("Customer: " + customer_name + "\n")
        file.write("Date: " + str(datetime.datetime.now()) + "\n")
        file.write("Items Purchased:\n")
        for line in total_invoice_lines:
            file.write(line + "\n")
        file.write("\nSubtotal: Rs " + str(grand_total) + "\n")
        file.write("VAT (15%): Rs " + str(vat) + "\n")
        file.write("Grand Total: Rs " + str(amount_to_pay) + "\n")
        
    print("\nInvoice generated: " + invoice_name)

def generate_restock_invoice(supplier, items_bought, total_amount):
    now = datetime.datetime.now()
    invoice_name = "restock_" + supplier + "_" + str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second) + ".txt"
    
    with open(invoice_name, "w") as file:
        file.write("Supplier: " + supplier + "\n")
        file.write("Date: " + str(datetime.datetime.now()) + "\n")
        file.write("Total Amount Spent: Rs " + str(total_amount) + "\n\n")
        for item in items_bought:
            file.write(item['Product'] + " | " + item['Brand'] + " | Qty: " + str(item['Qty']) + " | Rate: Rs" + str(item['Rate']) + " | Total: Rs" + str(item['Total']) + "\n")
    
    print("Restock invoice generated: " + invoice_name)
