def greedy_algorithm(items, budget):
    """Жадібний алгоритм для вибору страв з максимальним співвідношенням калорій до вартості"""
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    
    selected_items = []
    total_calories = 0
    total_cost = 0

    for item, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            selected_items.append(item)
            total_calories += data["calories"]
            total_cost += data["cost"]

    return selected_items, total_calories, total_cost


def dynamic_programming(items, budget):
    """Динамічне програмування для знаходження оптимального набору страв"""
    names = list(items.keys())
    costs = [items[name]["cost"] for name in names]
    calories = [items[name]["calories"] for name in names]
    n = len(names)

    # Створюємо таблицю для динамічного програмування
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Визначаємо, які страви були обрані
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(names[i - 1])
            w -= costs[i - 1]

    total_calories = dp[n][budget]
    total_cost = sum(items[item]["cost"] for item in selected_items)

    return selected_items, total_calories, total_cost


# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Бюджет
budget = 80

# Виконання жадібного алгоритму
greedy_result = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print(f"Вибрані страви: {greedy_result[0]}")
print(f"Загальна калорійність: {greedy_result[1]}")
print(f"Витрачено грошей: {greedy_result[2]}")

# Виконання динамічного програмування
dp_result = dynamic_programming(items, budget)
print("\nДинамічне програмування:")
print(f"Вибрані страви: {dp_result[0]}")
print(f"Загальна калорійність: {dp_result[1]}")
print(f"Витрачено грошей: {dp_result[2]}")
