def greedy_algorithm(items, budget):
    # Створення списку відсортованих за співвідношенням калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    selected_items = []
    total_cost = 0
    total_calories = 0
    
    # Вибір страви, доки бюджет не буде перевищений
    for item_name, item_info in sorted_items:
        if total_cost + item_info['cost'] <= budget:
            selected_items.append(item_name)
            total_cost += item_info['cost']
            total_calories += item_info['calories']
    
    return selected_items, total_cost, total_calories

# Дані про страви
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Бюджет
budget = 100

# Виклик функції жадібного алгоритму
selected_items, total_cost, total_calories = greedy_algorithm(items, budget)

print("Greedy Algorithm Results:")
print("Selected Items:", selected_items)
print("Total Cost:", total_cost)
print("Total Calories:", total_calories)
