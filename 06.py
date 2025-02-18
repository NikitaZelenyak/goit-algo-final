def greedy_algorithm(items, budget):
    """Жадібний алгоритм: вибираємо страви за найбільшим співвідношенням калорій/вартість"""
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    total_calories = 0
    selected_items = []
    remaining_budget = budget

    for item, data in sorted_items:
        if data["cost"] <= remaining_budget:
            selected_items.append(item)
            total_calories += data["calories"]
            remaining_budget -= data["cost"]

    return selected_items, total_calories


def dynamic_programming(items, budget):
    """Динамічне програмування: максимізація калорій у межах бюджету (подібне до задачі про рюкзак)"""
    item_names = list(items.keys())
    costs = [items[name]["cost"] for name in item_names]
    calories = [items[name]["calories"] for name in item_names]
    n = len(items)

    # DP-таблиця (рядки — предмети, стовпці — бюджет)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Заповнюємо DP-таблицю
    for i in range(1, n + 1):
        for b in range(budget + 1):
            if costs[i - 1] <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][b] = dp[i - 1][b]

    # Відновлення вибраних предметів
    selected_items = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:  # Якщо взяли цей предмет
            selected_items.append(item_names[i - 1])
            b -= costs[i - 1]

    selected_items.reverse()  # Відновлений порядок

    return selected_items, dp[n][budget]


# 🔹 Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# 🔹 Приклад запуску
budget = 60

greedy_result = greedy_algorithm(items, budget)
dp_result = dynamic_programming(items, budget)

print(f"🔹 Жадібний алгоритм: {greedy_result[0]}, калорії: {greedy_result[1]}")
print(f"🔹 Динамічне програмування: {dp_result[0]}, калорії: {dp_result[1]}")
