import matplotlib.pyplot as plt
import numpy as np
import random


def simulate_dice_rolls(num_rolls=100000):
    sums = {i: 0 for i in range(2, 13)}
    for _ in range(num_rolls):
        roll_sum = random.randint(1, 6) + random.randint(1, 6)
        sums[roll_sum] += 1
    return {k: v / num_rolls for k, v in sums.items()}


def visualize_dice_probabilities(probabilities):
    labels = list(probabilities.keys())
    values = list(probabilities.values())
    expected_values = [
        1 / 36,
        2 / 36,
        3 / 36,
        4 / 36,
        5 / 36,
        6 / 36,
        5 / 36,
        4 / 36,
        3 / 36,
        2 / 36,
        1 / 36,
    ]

    x = np.arange(len(labels))
    width = 0.35

    plt.figure(figsize=(10, 6))
    plt.bar(
        x - width / 2,
        values,
        width,
        label="Monte Carlo",
        color="lime",
        edgecolor="lime",
        linewidth=1.2,
    )
    plt.bar(
        x + width / 2,
        expected_values,
        width,
        label="Theoretical",
        color="fuchsia",
        edgecolor="fuchsia",
        linewidth=1.2,
    )

    plt.xlabel("Sum of Two Dice")
    plt.ylabel("Probability")
    plt.title("Comparison of Simulated and Theoretical Dice Roll Probabilities")
    plt.xticks(ticks=x, labels=labels)
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


dice_probabilities = simulate_dice_rolls()


print("Simulated Dice Probabilities:", dice_probabilities)

visualize_dice_probabilities(dice_probabilities)
