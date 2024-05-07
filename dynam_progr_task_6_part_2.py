def dynamic_programming(items, budget):
    # Ініціалізуємо матрицю
    dp = [[0] * (budget + 1) for _ in range(len(items) + 1)]
    
    # Заповнюємо матрицю
    for i, (item_name, item_info) in enumerate(items.items(), start=1):
        for j in range(1, budget + 1):
            if item_info['cost'] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - item_info['cost']] + item_info['calories'])
            else:
                dp[i][j] = dp[i - 1][j]
    
    # Відновлюємо вибрані страви
    selected_items = []
    i, j = len(items), budget
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(list(items.keys())[i - 1])
            j -= items[list(items.keys())[i - 1]]['cost']
        i -= 1
    
    return selected_items, dp[-1][-1]

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

# Виклик функції алгоритму динамічного програмування
selected_items, total_calories = dynamic_programming(items, budget)

print("Dynamic Programming Results:")
print("Selected Items:", selected_items)
print("Total Calories:", total_calories)
