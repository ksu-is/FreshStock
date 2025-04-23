# Code will start here: v1 
import json
import os
file_name = "fridge_inventory.json"
fridge = {}
shopping_list = []

if os.path.exists(file_name):
    with open(file_name, 'r') as file:
        fridge = json.load(file)
else:
    fridge = {}

# Feature to add items to the fridge
def add_item():
    name = input("Enter the item name: ")
    quantity = int(input("Enter the quantity: "))
    fridge[name] = quantity
    print(name + " (" + str(quantity) + ") added to the fridge.")

# Feature to remove items from the fridge
def remove_item():
    name = input("Enter the item you want to remove: ")
    if name in fridge:
        quantity = int(input("Enter quantity to remove (currently " + str(fridge[name]) + "): "))
        if quantity <= fridge[name]:
            fridge[name] -= quantity
            print(str(quantity) + " of " + name + " removed from the fridge.")
            if fridge[name] == 0:
                del fridge[name]  # Remove the item completely if it's out of stock
        else:
            print("You don't have enough of that item.")
    else:
        print(name + " is not in the fridge.")

# Feature to view fridge content
def view_fridge():
    if not fridge:
        print("The fridge is empty.")
    else:
        print("Item in fridge:")
        for name, quantity in fridge.items():
            print(name + ": " + str(quantity))

# Feature to edit items
def edit_item():
    name = input("Enter the item you want to change: ")
    if name in fridge:
        new_qty = int(input("Enter the new quantity of this item: "))
        fridge[name] = new_qty
        print("You now have" + str(new_qty) + "of" + name)
    else:
        print(name + "does not exist in the fridge.")

# Feature to produce a shopping list
def generate_shopping_list():
    empty_items = []
    for item, qty in fridge.items():
        if qty == 0:
            empty_items.append(item)

# Saving the fridge
def save_fridge():
    with open(file_name, 'w') as file:
        json.dump(fridge, file)

# Selection menu
def main():
    while True:
        print("Welcome to FreshStock!")
        print("\n--- Menu ---")
        print("1. Add item")
        print("2. Remove item")
        print("3. View fridge")
        print("4. Edit item")
        print("5. Show shopping list")
        print("6. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
                add_item()
        elif choice == '2':
                remove_item()
        elif choice == '3':
                view_fridge()
        elif choice == '4':
                edit_item()
        elif choice == '5':
                generate_shopping_list()
        elif choice == '6':
            save_fridge()
            print("Fridge saved. Goodbye!")
            break
        else:
            print("Please choose a number from 1 to 6.")

main()
