import matplotlib.pyplot as plt
import math

def draw_pifagor_tree(x, y, length, angle, level):
    if level == 0:
        return
    
    # Координати кінця гілки
    x_end = x + length * math.cos(math.radians(angle))
    y_end = y + length * math.sin(math.radians(angle))
    
    # Малюємо гілку
    plt.plot([x, x_end], [y, y_end], color='brown')
    
    # Рекурсивно малюємо ліву та праву гілки
    draw_pifagor_tree(x_end, y_end, length * 0.7, angle - 45, level - 1)
    draw_pifagor_tree(x_end, y_end, length * 0.7, angle + 45, level - 1)

# Вхідні параметри
x_start, y_start = 0, 0  # Початкові координати
length = 100  # Довжина початкової гілки
angle = 90  # Кут початкової гілки
level = int(input("Введіть рівень рекурсії: "))  # Рівень рекурсії

# Створення нового зображення та осей
plt.figure(figsize=(8, 8))
plt.axis('equal')

# Виклик рекурсивної функції для малювання дерева Піфагора
draw_pifagor_tree(x_start, y_start, length, angle, level)

# Налаштування відображення
plt.title("Pifagor Tree Fractal")
plt.axis('off')

# Показати зображення
plt.show()
