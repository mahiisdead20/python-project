# Micro Marketplace 

items = []   # list to store marketplace items


def add_item():
    print("\n--- Add Item ---")
    name = input("Enter item name: ")
    price = input("Enter item price: ")
    seller = input("Enter your name: ")

    item = {
        "name": name,
        "price": price,
        "seller": seller
    }
    items.append(item)
    print("Item added successfully!")


def view_items():
    print("\n--- All Marketplace Items ---")
    if len(items) == 0:
        print("No items available!")
        return

    for i, item in enumerate(items, start=1):
        print(f"{i}. {item['name']} - Rs.{item['price']} (Seller: {item['seller']})")


def search_item():
    print("\n--- Search Item ---")
    key = input("Enter item name to search: ").lower()

    found = False
    for item in items:
        if key in item["name"].lower():
            print(f"Found: {item['name']} - Rs.{item['price']} (Seller: {item['seller']})")
            found = True

    if not found:
        print("No matching item found.")


def buy_item():
    print("\n--- Buy Item ---")
    view_items()

    if len(items) == 0:
        return

    choice = int(input("Enter the item number to buy: "))
    if 1 <= choice <= len(items):
        bought = items.pop(choice - 1)
        print(f"You bought {bought['name']} for Rs.{bought['price']}!")
    else:
        print("Invalid choice.")


def menu():
    while True:
        print("\n====== MICRO MARKETPLACE ======")
        print("1. Add Item")
        print("2. View Items")
        print("3. Search Item")
        print("4. Buy Item")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            view_items()
        elif choice == "3":
            search_item()
        elif choice == "4":
            buy_item()
        elif choice == "5":
            print("Thank you for using Micro Marketplace!")
            break
        else:
            print("Invalid choice! Please try again.")


menu()
