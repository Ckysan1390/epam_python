def calculate_total(item_costs, items):
    """
    Calculates the total cost of items in the user's list and adds a 9% tax at the end.

    Parameters:
    item_costs: A dictionary mapping item names to their prices.
    user_items: A list of item names selected by the user.

    Returns:
    The total cost of the selected items including tax, rounded to two decimal places.
    """

    subtotal = 0
    for item in items:
        if item in item_costs:
          subtotal += item_costs[item]

    tax_amount = subtotal * 0.09
    total_cost_with_tax = subtotal + tax_amount

    return round(total_cost_with_tax, 2)

item_costs = {'apple': 1.5, 'banana': 0.75, 'orange': 1.25, 'grape': 1.75, 'kiwi': 2.25}
for item_name in item_costs.keys():
    print(item_name, end=' ')
selected_items = input("\nEnter a list of items separated by commas from the options above: ").replace(" ","").split(',')

total_cost = calculate_total(item_costs, selected_items)
print("Total cost with tax:", total_cost)