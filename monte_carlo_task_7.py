import random
import matplotlib.pyplot as plt

def roll_dice():
    return random.randint(1, 6)

def monte_carlo_simulation(num_trials):
    results = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_trials):
        dice1 = roll_dice()
        dice2 = roll_dice()
        total = dice1 + dice2
        results[total] += 1
    
    probabilities = {key: value / num_trials * 100 for key, value in results.items()}
    
    return probabilities

def print_probabilities(probabilities):
    print("Сума\tІмовірність")
    for total, probability in probabilities.items():
        print(f"{total}\t{probability:.2f}% ({probabilities[total]}/{num_trials})")

num_trials = 1000000  # Велика кількість кидків кубиків

probabilities = monte_carlo_simulation(num_trials)

print_probabilities(probabilities)


# Дані з результатами симуляції
sums = list(range(2, 13))


# Побудова графіку
plt.figure(figsize=(10, 6))
plt.bar(sums, probabilities, color='skyblue')

# Додавання підписів
plt.title('Ймовірності сум при киданні двох кубиків')
plt.xlabel('Сума')
plt.ylabel('Ймовірність, %')

# Відображення графіку
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()