# Code Chunking Activity

## Inventory Management System

inventory = []

print("Simple Inventory Management System")
print("=================================")

while True:
    print("\nMenu:")
    print("1. Add item")
    print("2. View all items")
    print("3. Search for item")
    print("4. Update item quantity")
    print("5. Remove item")
    print("6. Exit")
    
    choice = input("\nEnter your choice (1-6): ")
    
    if choice == "1":
        item_name = input("Enter item name: ")
        
        item_exists = False
        for item in inventory:
            if item["name"].lower() == item_name.lower():
                item_exists = True
                print(f"Error: {item_name} already exists in inventory!")
                break
                
        if not item_exists:
            try:
                quantity = int(input("Enter quantity: "))
                price = float(input("Enter price per unit: $"))
                
                if quantity < 0 or price < 0:
                    print("Error: Quantity and price must be positive numbers!")
                else:
                    new_item = {
                        "name": item_name,
                        "quantity": quantity,
                        "price": price
                    }
                    
                    inventory.append(new_item)
                    print(f"{item_name} added to inventory.")
            except ValueError:
                print("Error: Please enter numeric values for quantity and price!")
    
    elif choice == "2":
        if not inventory:
            print("Inventory is empty.")
        else:
            print("\nCurrent Inventory:")
            print("------------------")
            print(f"{'Item':<15}{'Quantity':<10}{'Price':<10}{'Value':<10}")
            print("-" * 45)
            
            total_value = 0
            for item in inventory:
                value = item["quantity"] * item["price"]
                total_value += value
                print(f"{item['name']:<15}{item['quantity']:<10}${item['price']:<9.2f}${value:<9.2f}")
            
            print("-" * 45)
            print(f"Total Inventory Value: ${total_value:.2f}")
    
    elif choice == "3":
        if not inventory:
            print("Inventory is empty.")
        else:
            search_term = input("Enter item name to search: ")
            found = False
            
            for item in inventory:
                if search_term.lower() in item["name"].lower():
                    if not found:
                        print("\nSearch Results:")
                        print(f"{'Item':<15}{'Quantity':<10}{'Price':<10}")
                        print("-" * 35)
                        found = True
                    
                    print(f"{item['name']:<15}{item['quantity']:<10}${item['price']:<9.2f}")
            
            if not found:
                print(f"No items found matching '{search_term}'")
    
    elif choice == "4":
        if not inventory:
            print("Inventory is empty.")
        else:
            item_name = input("Enter item name to update: ")
            found = False
            
            for item in inventory:
                if item["name"].lower() == item_name.lower():
                    found = True
                    print(f"Current quantity of {item_name}: {item['quantity']}")
                    
                    try:
                        new_quantity = int(input("Enter new quantity: "))
                        
                        if new_quantity < 0:
                            print("Error: Quantity must be a positive number!")
                        else:
                            item["quantity"] = new_quantity
                            print(f"{item_name} quantity updated to {new_quantity}.")
                    except ValueError:
                        print("Error: Please enter a numeric value for quantity!")
                    
                    break
            
            if not found:
                print(f"Error: {item_name} not found in inventory!")
    
    elif choice == "5":
        if not inventory:
            print("Inventory is empty.")
        else:
            item_name = input("Enter item name to remove: ")
            found = False
            
            for i, item in enumerate(inventory):
                if item["name"].lower() == item_name.lower():
                    found = True
                    del inventory[i]
                    print(f"{item_name} removed from inventory.")
                    break
            
            if not found:
                print(f"Error: {item_name} not found in inventory!")
    
    elif choice == "6":
        print("Thank you for using the Inventory Management System. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")


## Questions

# 1. How many logical chunks do you see in this code?

# 2. What would good labels/descriptions of those chunks be?

# 3. Write a comment to name the chunk of code