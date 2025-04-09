# Code will start here: v1 

fridge = {}
shopping_list = []

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

        
