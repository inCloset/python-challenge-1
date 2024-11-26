menu = {
    "Snacks": {"Cookie": 0.99, "Banana": 0.69, "Apple": 0.49, "Granola bar": 1.99},
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {"Cheese": 8.99, "Pepperoni": 10.99, "Vegetarian": 9.99},
        "Burger": {"Chicken": 7.49, "Beef": 8.49},
    },
    "Drinks": {
        "Soda": {"Small": 1.99, "Medium": 2.49, "Large": 2.99},
        "Tea": {"Green": 2.49, "Thai iced": 3.99, "Irish breakfast": 2.49},
        "Coffee": {"Espresso": 2.99, "Flat white": 2.99, "Iced": 3.49},
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {"New York": 4.99, "Strawberry": 6.49},
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49,
    },
}
customer_order = []

print("Welcome to the variety food truck.")
place_order = True
while place_order:
    print("From which menu would you like to order? ")
    i = 1
    menu_items = {}
    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key
        i += 1
    menu_category = input("Type menu number: ")
    if menu_category.isdigit():
        if int(menu_category) in menu_items.keys():
            menu_category_name = menu_items[int(menu_category)]
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2,
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {"Item name": key, "Price": value}
                    i += 1
            order_number = input("\nSelect a number for your order: ")
            if isinstance(order_number, str) and int(order_number) in menu_items:
                order_number = int(order_number)
                item_name = menu_items[order_number]
                try:
                    quantity_to_order = int(
                        input("Please select the quantity amount: ")
                    )
                    if quantity_to_order <= 0:
                        raise ValueError
                except ValueError:
                    print("Invalid quantity. Defaulting your quantity to 1.")
                    quantity_to_order = 1
                menu_items[order_number].setdefault("Quantity", quantity_to_order)
                customer_order.append(
                    {
                        "Item name": item_name.get('Item name'),
                        "Price": item_name.get('Price'),
                        "Quantity": item_name.get('Quantity'),
                    }
                )
                print(
                    f'Your {menu_items[order_number].get('Item name')} order has {quantity_to_order} quantities'
                )
        else:
            print(f"{menu_category} was not a menu option.")
    else:
        print("You didn't select a number.")

    while place_order:
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o")
        match keep_ordering.lower():
            case "y" | "yes":
                place_order = True
                break
            case "n" | "no":
                place_order = False
                break
            case "":
                print("customer provided an empty value.")
                place_order = True
                break
if customer_order:
    print("This is what we are preparing for you.\n")
    print("Item name                 | Price  | Quantity")
    print("--------------------------|--------|----------")
    for customer_item in customer_order:
        num_item_spaces = 28 - len(customer_item["Item name"]) - 3
        item_spaces = " " * num_item_spaces
        num_price_spaces = 8 - len(str(customer_item["Price"])) - 3
        price_spaces = " " * num_price_spaces
        print(
            f"{customer_item.get('Item name')}{item_spaces} | ${round(customer_item.get('Price'), 2)}{price_spaces} | {customer_item.get('Quantity')}"
        )
    total_order_price = sum(
        [order["Price"] * order["Quantity"] for order in customer_order]
    )
    print(f"Total Price:${round(total_order_price)}")
