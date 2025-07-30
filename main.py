from read import load_products
from write import save_products, generate_invoice, generate_restock_invoice
from operations import display_products, process_sale, restock_products

PRODUCT_FILE = "products.txt"
print("\n")
print("\n")
print("------------------------------------------------------------------------")
print("\t \tWholesale SkinCare Management Shop")
print("\n")
print("\t \t \tSafal's Shop")
print("\n")
print("------------------------------------------------------------------------")
print("\t \tWelcome to my wholesale SkinCare SHOP")
print("------------------------------------------------------------------------")
print("\n")

# Load products
products = load_products(PRODUCT_FILE)

# Main menu loop
while True:
    print("\nMain Menu:")
    print("1. View Products")
    print("2. Sell Product")
    print("3. Buy Products (Restock)")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_products(products)
    elif choice == "2":
        result = process_sale(products)
        if result:
            customer_name, total_invoice_lines, grand_total, vat, amount_to_pay = result
            generate_invoice(customer_name, total_invoice_lines, grand_total, vat, amount_to_pay)
            save_products(PRODUCT_FILE, products)
    elif choice == "3":
        supplier, items_bought, total_amount = restock_products(products)
        if supplier:
            generate_restock_invoice(supplier, items_bought, total_amount)
            save_products(PRODUCT_FILE, products)
    elif choice == "4":
        save_products(PRODUCT_FILE, products)
        print("\nExiting program...")
        print("Thank you for using the program!")
        break
    else:
        print("Invalid choice. Please try again.")
