# TermProject.py
#
# Mike's Bikes Store Management System
#

# Importing Libraries

from datetime import datetime
import os



            #######################
            ## Global Data Lists ##
            #######################

customers = []
inventory = []
orders = []

            #############
            ## Classes ##
            #############

class Customer:
    def __init__(self, customer_id, name, phone, email, status): # adding customer class with attributes
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email
        self.status = status


class Product:
    def __init__(self, product_id, name, category, color, size, price, stock): # adding product class with attributes
        self.product_id = product_id
        self.name = name
        self.category = category
        self.color = color
        self.size = size
        self.price = price
        self.stock = stock


class Order:
    def __init__(self, order_id, customer_id, product_id, quantity, total): # adding order class with attributes
        self.order_id = order_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.total = total
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")



            ##########################
            ## Sample Starting Data ##
            ##########################

# Adding in customer data to show for proof of concept

customers.append(Customer(1, "John Smith", "555-1111", "john@email.com", "Normal"))
customers.append(Customer(2, "Sarah Jones", "555-2222", "sarah@email.com", "Premium"))
customers.append(Customer(3, "Mike Brown", "555-3333", "mike@email.com", "Elite"))

# Adding in inventory data to show for proof of concept

inventory.append(Product(101, "Mountain Bike", "Bike", "Red", "Large", 599.99, 5))
inventory.append(Product(102, "Road Bike", "Bike", "Blue", "Medium", 799.99, 3))
inventory.append(Product(103, "Helmet", "Accessory", "Black", "Medium", 49.99, 10))
inventory.append(Product(104, "Gloves", "Accessory", "Gray", "Large", 19.99, 8))

            ########################
            ## Customer Functions ##
            ########################

def add_customer(): # adding a new customer
    try:
        customer_id = int(input("Enter Customer ID: "))
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        status = input("Enter Status (Normal/Premium/Elite): ")

        # adding customer to database (would need to add functionality to save data)
        customers.append(Customer(customer_id, name, phone, email, status))
        print("Customer added successfully.")

    except:
        print("Invalid customer information.") # try....except lines add error message upon invalid input


def view_customers():
    if not customers:
        print("No customers found.")
        return

    for c in customers:
        print(c.customer_id, c.name, c.phone, c.email, c.status)

            #########################
            ## Inventory Functions ##
            #########################
        
def add_product():
    try:
        product_id = int(input("Enter Product ID: "))
        name = input("Enter Product Name: ")
        category = input("Enter Category: ")
        color = input("Enter Color: ")
        size = input("Enter Size: ")
        price = float(input("Enter Price: "))
        stock = int(input("Enter Stock Quantity: "))

        inventory.append(Product(product_id, name, category, color, size, price, stock))
        print("Product added successfully.")

    except:
        print("Invalid product information.") # try...except lines add error message upon invalid input


def view_inventory():
    if not inventory:
        print("Inventory is empty.")
        return

    for p in inventory:
        print(
            p.product_id,
            p.name,
            p.category,
            p.color,
            p.size,
            "$" + str(p.price),
            "Stock:",
            p.stock
        )

            #####################
            ## Order Functions ##
            #####################

def create_order():
    if not customers:
        print("Cannot create order. No customers available.")
        return

    if not inventory:
        print("Cannot create order. No inventory available.")
        return

    try:
        order_id = len(orders) + 1
        customer_id = int(input("Enter Customer ID: "))
        product_id = int(input("Enter Product ID: "))
        quantity = int(input("Enter Quantity: "))

        customer_found = False
        product_found = None

        for c in customers:
            if c.customer_id == customer_id:
                customer_found = True

        if not customer_found:
            print("Invalid Customer ID.")
            return

        for p in inventory:
            if p.product_id == product_id:
                product_found = p

        if product_found is None:
            print("Invalid Product ID.")
            return

        if quantity > product_found.stock:
            print("Item Out of Stock.")
            return

        total = quantity * product_found.price # Updating Total
        product_found.stock -= quantity # Updating quantity of item in stock

        orders.append(Order(order_id, customer_id, product_id, quantity, total)) # Creating the order
        print("Order created successfully.")
        print("Total: $", total)

    except:
        print("Invalid order entry.") # try...except lines add error message upon invalid input

            #############
            ## Reports ##
            #############
        
def sales_report():
    total_sales = 0

    for o in orders:
        total_sales += o.total

    print("Total Orders:", len(orders))
    print("Total Sales: $", total_sales)

            ###########
            ## Menus ##
            ###########

def customer_menu():
    while True:
        
        print("\n--- Customer Menu ---")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Back")

        choice = input("Choose option: ")

        if choice == "1":
            add_customer()
        elif choice == "2":
            view_customers()
        elif choice == "3":
            break
        else:
            print("Invalid Menu Choice.")


def inventory_menu():
    while True:
        
        print("\n--- Inventory Menu ---")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. Back")

        choice = input("Choose option: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            break
        else:
            print("Invalid Menu Choice.")


def order_menu():
    while True:
        
        print("\n--- Order Menu ---")
        print("1. Create Order")
        print("2. Back")

        choice = input("Choose option: ")

        if choice == "1":
            create_order()
        elif choice == "2":
            break
        else:
            print("Invalid Menu Choice.")


            # ---------------------------- #
            #        Main Function         #
            # ---------------------------- #

# Creating the Main Menu; this will come up when the program is launched

def main():
    splash_screen()
    
    while True:
        print("\n=== Mike's Bikes ===")
        print("1. Customers")
        print("2. Inventory")
        print("3. Orders")
        print("4. Reports")
        print("5. Exit")

        choice = input("Choose option: ") # Prompts user for menu selection which routes program flow to the appropriate function

        if choice == "1":
            customer_menu()
        elif choice == "2":
            inventory_menu()
        elif choice == "3":
            order_menu()
        elif choice == "4":
            sales_report()
        elif choice == "5":
            print("Thank you for using Mike's Bikes.")
            break
        else:
            print("Invalid Menu Choice.")

def splash_screen():

    width = 80 # standard console width target

    print("\n" * 2)



    print(" __  __ _ _        _       ____  _ _             ".center(width))
    print("|  \/  (_) | _____( )___  | __ )(_) | _____  ___ ".center(width))
    print("| |\/| | | |/ / _ \// __| |  _ \| | |/ / _ \/ __|".center(width))
    print('| |  | | |   <  __/ \__ \ | |_) | |   <  __/\__ \\'.center(width))
    print("|_|  |_|_|_|\_\___| |___/ |____/|_|_|\_\___||___/".center(width))


    print("\n")

    print("M I K E ' S   B I K E S".center(width))
    print("Store Mangement System".center(width))
    print("\"Ride the Future\"".center(width))
                                                  
    print("\n")

    print("                                                    .'  `.                  ".center(width))
    print("                                                   /      \                 ".center(width))
    print("                     o                            /        |                ".center(width))
    print("                      8ooooooooo               __________  |                ".center(width))
    print("                        ``8'                  /.-------. \ |                ".center(width))
    print("                         |`                   ||      ` ` |&lt;             ".center(width))
    print("                          `|___________________\\      |||| )               ".center(width))
    print("                          / _____________________\ ._._.'.'(                ".center(width))
    print("                         / |                     \\ ``--'                   ".center(width))
    print("                        //|`                      \\                        ".center(width))
    print("                       //  `|                      \\                       ".center(width))
    print("                      //   |`                      . \                      ".center(width))
    print("         .d888888b.  //     `|                   .'.'\\  .d888888b.         ".center(width))
    print("      o8Y'   .    `Y//      |`                  / /   \\Y'    .  .`Y8o      ".center(width))
    print("    oY'   .  .   . //Y8o     `|               .'.'  dY'\\  .  .     .`Yo    ".center(width))
    print("   dY  .     .    //   Yb    |`              / /   dY.  \\    .    .  .Yb   ".center(width))
    print("  dY .  .  . .  .//   . Yb    `|           .'.'   dY   . \\ . . . .     Yb  ".center(width))
    print(" oY.   . .   .  //  .    Yb   |`          / /    oY .    .\\  .  . .   . Yo ".center(width))
    print("o8    .   .  . // .    .  8b   `| =.=   .'.'    o8     .   \\ . .   .     8o".center(width))
    print("8Y  .    . . .//__________Y8___|`_____ / /      8P  .     . \\.. .     .  Y8".center(width))
    print("8............@/__ ........ 8   .'.  ..`.'       8............\@)...........8".center(width))
    print("8    .   . (`-.__`--.__   d8  /. . |..  \       8     .  .  . . . .     .  8".center(width))
    print("8b    .    .(@   `--.__`--.__|....  .... |      8b.    .   .  .  .   .    d8".center(width))
    print("Y8 .    . .  `-._      `--.__|..   @     |      Y8   .  . . . . . . .  .  8Y".center(width))
    print(" Yb   .  .   .  .`-._   dP   |.... |.    |       Yb.     .    .    .     dP ".center(width))
    print("  Yb.   .  . . . .   `-dP     \  . |... /         Yb .  .  .  .  .  .  .dP  ".center(width))
    print("   Yo. .     .    .  .oP `--.__`.__|__.'           Yo. .      .      ..oP   ".center(width))
    print("    `8o.  .  .  .  .o8'            |                `8o.  .   .   . .o8'    ".center(width))
    print("      `Y88booood888P'             =.=                 `Y88boooood888P'      ".center(width))
    print('          """"""                                          """""""           '.center(width))

    print("\n")
      
    print("Welcome to Mike's Bikes!\n")
    input("Press Enter to continue...")
                                                  

#################
## Run Program ##
#################

main()
