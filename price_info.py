#price_info.py
price_list = {'apple': 1.20, 'orange': 1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear': 0.90, 'papaya': 2.95, 'pomegranate': 4.95}

quantity_list = {'apple': 5, 'orange': 5, 'watermelon': 1, 'pineapple': 2, 'pear': 10, 'papaya': 1, 'pomegranate': 2}

def total_cost_shopping():
    total_cost = 0
    for fruit, quantity in quantity_list.items():
        if fruit in price_list:
            cost = quantity * price_list[fruit]
            total_cost += cost
    return total_cost

def cost_of_fruits(fruit, quantity):
    if fruit in price_list:
        cost = quantity * price_list[fruit]
        return cost
    else:
        return f"{fruit} is not in the price list."

def main():
    cost_of_fruits('apple', 10)
    total_cost_shopping()

if __name__ == "__main__":
    main()