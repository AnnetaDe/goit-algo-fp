import matplotlib.pyplot as plt
import numpy as np


def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )
    total_calories = 0
    selected_items = []

    for item, values in sorted_items:
        if budget >= values["cost"]:
            selected_items.append(item)
            total_calories += values["calories"]
            budget -= values["cost"]

    return selected_items, total_calories


def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item_name, values = item_list[i - 1]
        cost = values["cost"]
        calories = values["calories"]
        for b in range(budget + 1):
            if cost > b:
                dp[i][b] = dp[i - 1][b]
            else:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)

    total_calories = dp[n][budget]
    selected_items = []
    b = budget

    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            item_name, values = item_list[i - 1]
            selected_items.append(item_name)
            b -= values["cost"]

    return selected_items, total_calories


def visualize_results(greedy_result, dp_result):
    labels = list(set(greedy_result[0] + dp_result[0]))
    greedy_values = [
        items[item]["calories"] if item in greedy_result[0] else 0 for item in labels
    ]
    dp_values = [
        items[item]["calories"] if item in dp_result[0] else 0 for item in labels
    ]
    x = np.arange(len(labels))

    plt.figure(figsize=(10, 6))
    width = 0.35

    plt.bar(
        x - width / 2,
        greedy_values,
        width,
        label="Greedy",
        color="orange",
        edgecolor="orange",
        linewidth=1.2,
    )
    plt.bar(
        x + width / 2,
        dp_values,
        width,
        label="Dynamic Programming",
        color="red",
        edgecolor="red",
        linewidth=1.2,
    )

    plt.xlabel("Selected Items")
    plt.ylabel("Calories")
    plt.title(" Greedy and Dynamic Programming Approaches")
    plt.xticks(ticks=x, labels=labels)
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}

budget = 100
greedy_result = greedy_algorithm(items, budget)
dp_result = dynamic_programming(items, budget)

print("Greedy Algorithm Result:", greedy_result)
print("Dynamic Programming Result:", dp_result)

visualize_results(greedy_result, dp_result)
