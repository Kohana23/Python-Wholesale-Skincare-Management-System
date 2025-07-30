**# Wholesale SkinCare Management Shop**

**## **Overview****

This is a Python-based wholesale skincare management system designed to help shop owners manage their inventory, process sales, and handle restocking operations efficiently. The system features:

- Product inventory management
- Sales processing with automatic invoice generation
- Restocking functionality with supplier invoices
- VAT calculation (15%)
- Buy 2 Get 1 Free promotional offer implementation
- File-based data persistence

**## Features**

**### Inventory Management**
- View all products with details (name, brand, quantity, price, country of origin)
- Add new products to inventory
- Restock existing products
- Automatic price calculation (selling price = 2 × cost price)

**### Sales Processing**
- Process customer purchases
- Automatic "Buy 2 Get 1 Free" promotion calculation
- Invoice generation with:
  - Customer details
  - Itemized purchases
  - Subtotal
  - VAT (15%)
  - Grand total

**### Restocking System**
- Restock existing products
- Add new products to inventory
- Generate restock invoices with supplier details
- Update product costs and automatically adjust selling prices

**## File Structure
**
```
skincare_shop/
├── main.py            # Main program and menu system
├── operations.py      # Core business logic functions
├── read.py            # Product data loading functionality
├── write.py           # Data saving and invoice generation
└── products.txt       # Product database (created automatically)
```

**## How to Use**

1. Run `main.py` to start the program
2. Use the menu to:
   - View products
   - Process sales
   - Restock inventory
   - Exit the program

All data is automatically saved to `products.txt`, and invoices are generated as text files with timestamps.
**
## Requirements**

- Python 3.x
- No additional libraries required

**## Business Rules**

- Selling price is automatically set to 2 times the cost price
- VAT is calculated at 15% of the subtotal
- Promotion: Buy 2 items, get 1 free (applied automatically during sales)

**## Sample Invoices**

The system generates two types of invoices:
1. Customer invoices (for sales)
2. Restock invoices (for supplier purchases)
