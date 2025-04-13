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
        for name, quantity in fridge.items()L
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

# Saving the fridge
def save_fridge():
    with open(file_name, 'w') as file:
        json.dump(fridge, file)