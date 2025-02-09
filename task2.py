import numpy as np
import matplotlib.pyplot as plt
import random


class Tree:
    def __init__(self, size=10):
        self.root = None
        self.size = size
        self.cmap = plt.get_cmap("viridis")  # Use a gradient colormap

    class TreeNode:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.height = 1

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, z):
        y = z.left
        T2 = y.right
        y.right = z
        z.left = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, node, key):
        if not node:
            return self.TreeNode(key)
        if key < node.value:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balance = self.get_balance(node)

        if balance > 1 and key < node.left.value:
            return self.rotate_right(node)
        if balance < -1 and key > node.right.value:
            return self.rotate_left(node)
        if balance > 1 and key > node.left.value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and key < node.right.value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def add(self, key):
        self.root = self.insert(self.root, key)

    def _draw_pythagoras(self, ax, node, x, y, size, angle, depth=0):
        if not node:
            return

        angle_rad = np.radians(angle)
        color = self.cmap(depth / 10)

        p1 = np.array([x, y])
        p2 = np.array([x + size * np.cos(angle_rad), y + size * np.sin(angle_rad)])
        p3 = np.array(
            [
                x + size * np.cos(angle_rad) - size * np.sin(angle_rad),
                y + size * np.sin(angle_rad) + size * np.cos(angle_rad),
            ]
        )
        p4 = np.array([x - size * np.sin(angle_rad), y + size * np.cos(angle_rad)])

        square = np.array([p1, p2, p3, p4, p1])
        ax.fill(
            square[:, 0], square[:, 1], color=color, edgecolor="black", linewidth=1.2
        )

        new_size = size * np.sqrt(2) / 2
        rotation_angle = 45

        if node.left:
            left_x = p4[0]
            left_y = p4[1]
            print(left_x, left_y)
            left_x = p4[0]
            left_y = p4[1]
            self._draw_pythagoras(
                ax,
                node.left,
                left_x,
                left_y,
                new_size,
                angle + rotation_angle,
                depth + 1,
            )

        if node.right:
            right_x = p2[0]
            right_y = p2[1]
            self._draw_pythagoras(
                ax,
                node.right,
                right_x,
                right_y,
                new_size,
                angle - rotation_angle,
                depth + 1,
            )

    def draw_pythagoras(self, ax):
        ax.set_aspect("equal")
        ax.axis("off")
        self._draw_pythagoras(ax, self.root, x=0, y=0, size=self.size, angle=45)


if __name__ == "__main__":
    tree = Tree(size=10)
    leaves = [random.randint(1, 100) for _ in range(36)]

    for leaf in leaves:
        tree.add(leaf)

    fig, ax = plt.subplots(figsize=(10, 10))
    tree.draw_pythagoras(ax)
    plt.show()

    print("AVL-based Pythagoras Tree constructed with values:", leaves)
