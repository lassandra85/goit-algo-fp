import random
import matplotlib.pyplot as plt
import numpy as np

def monte_carlo_dice_simulation(n_rolls=100000):
    """Симуляція кидків двох кубиків методом Монте-Карло"""
    sums_count = {i: 0 for i in range(2, 13)}

    for _ in range(n_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice_sum = dice1 + dice2
        sums_count[dice_sum] += 1

    # Обчислення ймовірностей
    probabilities = {s: count / n_rolls for s, count in sums_count.items()}

    return probabilities

def plot_probabilities(probabilities):
    """Побудова графіка ймовірностей випадання сум"""
    theoretical_probs = {
        2: 1/36,  3: 2/36,  4: 3/36,  5: 4/36,  6: 5/36, 
        7: 6/36,  8: 5/36,  9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
    }

    sums = list(probabilities.keys())
    monte_carlo_vals = [probabilities[s] for s in sums]
    theoretical_vals = [theoretical_probs[s] for s in sums]

    x = np.arange(len(sums))

    plt.figure(figsize=(10, 5))
    plt.bar(x - 0.2, monte_carlo_vals, 0.4, label="Монте-Карло", color="skyblue")
    plt.bar(x + 0.2, theoretical_vals, 0.4, label="Аналітичні", color="orange")
    plt.xticks(x, sums)
    plt.xlabel("Сума на двох кубиках")
    plt.ylabel("Ймовірність")
    plt.legend()
    plt.title("Порівняння ймовірностей: Монте-Карло vs Аналітичні")
    plt.show()

# Виконання симуляції
probabilities = monte_carlo_dice_simulation(100000)

# Вивід результатів
print("Ймовірності випадіння кожної суми (Монте-Карло):")
for k, v in probabilities.items():
    print(f"Сума {k}: {v:.4f}")

# Побудова графіка
plot_probabilities(probabilities)
