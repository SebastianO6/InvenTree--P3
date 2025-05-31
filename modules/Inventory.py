from modules.item import Item
from lib.helpers import (
    display_menu,
    display_items,
    get_item_details,
    exit_program
)



def handle_view_all():
    items = Item.get_all()
    display_items(items)

def handle_add_item():
    print("\nAdd New Item")
    name, quantity, price, category, location = get_item_details()
    Item.create(name, quantity, price, category, location)
    print(f"\nItem '{name}' added")

def handle_update_item():
    print("\nUpdate Item")
    try:
        item_id = int(input("Item ID to update: ").strip())
    except ValueError:
        print("Invalid ID")
        return
    
    if item := Item.find_by_id(item_id):
        print("\nCurrent item:")
        display_items([item])
        name, quantity, price, category, location = get_item_details(item)
        
        item.name = name
        item.quantity = quantity
        item.price = price
        item.category = category
        item.location = location
        item.update()
        print("\nItem updated")
    else:
        print("\nItem not found")

def handle_delete_item():
    print("\nDelete Item")
    try:
        item_id = int(input("Item ID to delete: ").strip())
    except ValueError:
        print("Invalid ID")
        return
    
    if item := Item.find_by_id(item_id):
        item.delete()
        print("\nItem deleted")
    else:
        print("\nItem not found")

def handle_search():
    print("\nSearch Items")
    term = input("Search by name or category: ").strip()
    items = Item.find_by_name(term) + Item.find_by_category(term)
    display_items(items)

def main():
    Item.create_table()
    
    handlers = {
        '1': handle_view_all,
        '2': handle_add_item,
        '3': handle_update_item,
        '4': handle_delete_item,
        '5': handle_search,
        '6': exit_program
    }
    
    while True:
        display_menu()
        choice = input("\nEnter choice (1-6): ").strip()
        
        if handler := handlers.get(choice):
            handler()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
