import random
import matplotlib.pyplot as plt

def monte_carlo_dice_simulation(n_rolls=100000):
    """Метод Монте-Карло: кидаємо два кубики багато разів та рахуємо частоту сум"""
    
    sums_count = {i: 0 for i in range(2, 13)}

    for _ in range(n_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        sums_count[total] += 1

    probabilities = {s: count / n_rolls for s, count in sums_count.items()}
    
    return probabilities

# 🔹 Запускаємо симуляцію
n_rolls = 100000  # Чим більше кидків, тим точніші результати
simulated_probabilities = monte_carlo_dice_simulation(n_rolls)

# 🔹 Теоретичні ймовірності
theoretical_probabilities = {
    2: 1/36,  3: 2/36,  4: 3/36,  5: 4/36,  6: 5/36, 
    7: 6/36,  8: 5/36,  9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}

# 🔹 Відображення результатів
sums = list(range(2, 13))
simulated_values = [simulated_probabilities[s] for s in sums]
theoretical_values = [theoretical_probabilities[s] for s in sums]

plt.figure(figsize=(10, 6))
plt.bar(sums, simulated_values, width=0.4, label="Монте-Карло", color='royalblue', alpha=0.7)
plt.bar([s + 0.4 for s in sums], theoretical_values, width=0.4, label="Теоретична", color='orange', alpha=0.7)

plt.xlabel("Сума на кубиках")
plt.ylabel("Ймовірність")
plt.title(f"Порівняння симуляції Монте-Карло та теоретичних ймовірностей ({n_rolls} кидків)")
plt.xticks(sums)
plt.legend()
plt.show()
