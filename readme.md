# Food Truck Ordering System

## Steps to Implement the System

### 1. Set up the Order List
- Application creates a list to store dictionaries containing:
    - Menu item name
    - Item price
    - Quantity ordered
- Application launches the store and present a greeting to the customer.

### 2. Enable Continuous Ordering
- With the power of python loop we allow customers to order multiple items.

### 3. Display Menu Categories
- Application then prompts the customer which menu category they want to order from.
- Steps:
    - We create a variable for the menu item number.
    - We also create a dictionary to store the menu categories for later retrieval.
    - Display the options for customer to choose from (first-level dictionary keys in the menu).
    - Application then associates the menu category with its corresponding menu item number.
    - We also increment the menu item number by 1 for each category iteration.

### 4. Process Customer's Input for Menu Category
- Application validates customer entry for a number value:
    - If valid:
        - We check if the number corresponds to a menu category.
        - We then save the selected category name to a variable.
        - Present to the customer the menu category name selected by the customer.
        - Display the menu options within the selected category.
    - If invalid:
        - Inform the customer that the input isn't valid.

### 5. Ask Customer to Input Menu Item Number
- Prompt the customer to select a specific item from the displayed options.

### 6. Validate Customer's Input for Menu Item
- Application again validates customer entry for a number or digit entry:
    - We then convert the selection to an integer.
    - Application check to determine if the selection is valid within the menu items:
        - Store the item name and price as variables.
        - Ask the customer for the quantity of the selected item.
        - Validate the quantity:
            - Default to 1 if the quantity input is invalid.
        - Add the item name, price, and quantity to the order list.
    - If invalid:
        - Inform the customer that the input isn't valid.
        - Loop back to allow them to try again.

### 7. Ask if the Customer Wants to Continue Ordering
- Application prompts the customer with a "yes" or "no" option:
    - If "yes", continue the ordering process.
    - If "no":
        - Exit the loop.
        - Thank the customer for their order.

### 8. Print the Customer's Final Order
- Application then presents the customer with their order summary:
    - Item name
    - Price
    - Quantity

### 9. Structure the Output for Readability
- We again loop through the items in the customer's order to present the following.
- Use formatted printing to align:
    - Item names
    - Prices
    - Quantities

### 10. Calculate the Total Cost
- With the help of Python list comprehension we multiply the price by quantity for each item.
- Application then sums the total cost and display it to the customer.