class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    
    def get_cost(self):
        return self.cost
    
    def get_quantity(self):
        return self.quantity
    
    def __str__(self):
        return f"Country: {self.country}\nCode: {self.code}\nProduct: {self.product}\nCost: {self.cost}\nQuantity: {self.quantity}\n"

shoes_list = []

def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # Skip the first line
            for line in file:
                data = line.strip().split(",")
                country = data[0]
                code = data[1]
                product = data[2]
                cost = int(data[3])
                quantity = int(data[4])
                shoe = Shoe(country, code, product, cost, quantity)
                shoes_list.append(shoe)
    except FileNotFoundError:
        print("Inventory file not found.")

def capture_shoes():
    country = input("Enter the country: ")
    code = input("Enter the code: ")
    product = input("Enter the product: ")
    cost = int(input("Enter the cost: "))
    quantity = int(input("Enter the quantity: "))
    shoe = Shoe(country, code, product, cost, quantity)
    shoes_list.append(shoe)

def view_all():
    if len(shoes_list) == 0:
        print("No shoes in inventory.")
    else:
        for shoe in shoes_list:
            print(shoe)

def re_stock():
    if len(shoes_list) == 0:
        print("No shoes in inventory.")
        return

    min_quantity = min(shoe.quantity for shoe in shoes_list)
    low_stock_shoes = [shoe for shoe in shoes_list if shoe.quantity == min_quantity]

    print("Shoes with low stock:")
    for shoe in low_stock_shoes:
        print(shoe)

    for shoe in low_stock_shoes:
        response = input(f"Do you want to restock {shoe.product} ({shoe.quantity})? (y/n): ")
        if response.lower() == 'y':
            quantity_to_add = int(input("Enter the quantity to add: "))
            shoe.quantity += quantity_to_add
            print(f"{quantity_to_add} shoes added to {shoe.product}.")
        else:
            print(f"No restock for {shoe.product}.")

def search_shoe():
    code = input("Enter the shoe code: ")
    found_shoe = None
    for shoe in shoes_list:
        if shoe.code == code:
            found_shoe = shoe
            break
    if found_shoe:
        print("Shoe details:")
        print(found_shoe)
    else:
        print("Shoe not found.")

def value_per_item():
    if len(shoes_list) == 0:
        print("No shoes in inventory.")
    else:
        for shoe in shoes_list:
            value = shoe.cost * shoe.quantity
            print(f"Value for {shoe.product}: {value}")

def highest_qty():
    if len(shoes_list) == 0:
        print("No shoes in inventory.")
    else:
        max_quantity = max(shoe.quantity for shoe in shoes_list)
        max_quantity_shoe = [shoe for shoe in shoes_list if shoe.quantity == max_quantity]

        if len(max_quantity_shoe) == 1:
            print("Product with highest quantity:")
            print(max_quantity_shoe[0])
        else:
            print("Products with highest quantity:")
            for shoe in max_quantity_shoe:
                print(shoe)

def display_menu():
    print("Inventory Management System")
    print("1. Read shoes data from file")
    print("2. Capture shoe data")
    print("3. View all shoes")
    print("4. Re-stock shoes")
    print("5. Search for a shoe")
    print("6. Calculate value per item")
    print("7. Find product with highest quantity")
    print("8. Exit")

read_shoes_data()

while True:
    display_menu()
    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        read_shoes_data()
    elif choice == '2':
        capture_shoes()
    elif choice == '3':
        view_all()
    elif choice == '4':
        re_stock()
    elif choice == '5':
        search_shoe()
    elif choice == '6':
        value_per_item()
    elif choice == '7':
        highest_qty()
    elif choice == '8':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 8.")
