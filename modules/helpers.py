def display_menu():
    print("\n=== InvenTree Menu ===")
    print("1. View All Items")
    print("2. Add Item")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Search Items")
    print("6. Exit")

def display_items(items):
    if not items:
        print("\nNo items found")
        return
    
    print("\nID  Name    Qty  Price    Category     Location")
    print("-" * 60)
    for item in items:
        print(f"{item.id:<4}{item.name[:18]:<20}{item.quantity:<5}${item.price:<8.2f}{item.category or 'N/A':<13}{item.location or 'N/A'}")

def get_number(prompt, type_func):
    while True:
        try:
            value = type_func(input(prompt).strip())
            return value if value >= 0 else get_number("Must be positive. " + prompt, type_func)
        except ValueError:
            print("Please enter a valid number")

def get_item_details(item=None):
    name = input(f"Name [{item.name if item else ''}]: ").strip() if item else input("Name: ").strip()
    quantity = get_number(f"Quantity [{item.quantity if item else ''}]: ", int) if item else get_number("Quantity: ", int)
    price = get_number(f"Price [{f'${item.price:.2f}' if item else ''}]: $", float) if item else get_number("Price: $", float)
    category = input(f"Category [{item.category if item else ''}]: ").strip() or None if item else input("Category (optional): ").strip() or None
    location = input(f"Location [{item.location if item else ''}]: ").strip() or None if item else input("Location (optional): ").strip() or None
    
    return name or (item.name if item else ""), quantity, price, category, location

def exit_program():
    print("Goodbye!")
    exit()