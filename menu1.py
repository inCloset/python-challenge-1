# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}
# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
# Launch the store and present a greeting to the customer
# Customers may want to order multiple items, so let's create a continuous loop
# Ask the customer from which menu category they want to order
# Create a variable for the menu item number
# Print the options to choose from menu headings (all the first level
# dictionary items in menu).
# Get the customer's input
# menu_category = input("Type menu number: ")
# 2. Ask customer to input menu item number
# 3. Check if the customer typed a number
# Convert the menu selection to an integer
welcome_message = 'Welcome to the variety food truck.'
print(welcome_message)
place_order = True
menu_items = {}
menu_category_name = ''
item_name = ''
while place_order:
    print('Please select an item from the order menu')
    for menu_item_number, k in enumerate(menu.keys()):
        print (f'Item:{menu_item_number} {k}')
        menu_items[menu_item_number] = k
    menu_category = input("Type menu number: ")
    if isinstance(menu_category, str):
        menu_category = int(menu_category)

    if menu_category in menu_items.keys():
        menu_category_name = menu_items[menu_category]
        print(f'Customer selected {menu_category_name} item for their order.')

    if menu_category_name in menu.keys():
        item_name = menu[menu_category_name]
        print(item_name)

    quantity_to_order = input('How many quantities of items would you like purchase from this menu:')

    if not isinstance(quantity_to_order, int):
        quantity_to_order = 1
        dict(item_name).setdefault('Quantity', quantity_to_order)
        for item in item_name:
            print(item)
    else:
        for item in item_name:
            print(item)

# menu_selection = input(f'Attempts{attempt}Please let us know what you would like to order:' )




# 4. Check if the menu selection is in the menu items
    # Store the item name as a variable
    # Ask the customer for the quantity of the menu item
    # Check if the quantity is a number, default to 1 if not
    # Add the item name, price, and quantity to the order list
    # Tell the customer that their input isn't valid
    # Tell the customer they didn't select a menu option
