def helper_1():
    print("Performing useful function #1")

def exit_program():
    print("Goodbye!")
    exit()

def display_menu():
    print("\n--- Inventory Menu ---")
    print("1. View All Items")
    print("2. Add New Item")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Search Items")
    print("6. Exit")

def display_items(items):
    if not items:
        print("\nNo items found.")
    else:
        for item in items:
            print(f"ID: {item.id} | Name: {item.name} | Qty: {item.quantity} | Price: {item.price} | Category: {item.category} | Location: {item.location}")

def get_item_details(existing_item=None):
    name = input(f"Name [{getattr(existing_item, 'name', '')}]: ") or getattr(existing_item, 'name', '')
    quantity = input(f"Quantity [{getattr(existing_item, 'quantity', 0)}]: ") or getattr(existing_item, 'quantity', 0)
    price = input(f"Price [{getattr(existing_item, 'price', 0.0)}]: ") or getattr(existing_item, 'price', 0.0)
    category = input(f"Category [{getattr(existing_item, 'category', '')}]: ") or getattr(existing_item, 'category', '')
    location = input(f"Location [{getattr(existing_item, 'location', '')}]: ") or getattr(existing_item, 'location', '')
    return name, int(quantity), float(price), category, location
