from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional[Node] = None


class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def search_element(self, data) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def display_full(self):
        current = self.head
        visited = set()  # To track visited nodes
        cycle_detected = False

        while current:
            if current in visited:
                print(f"{current.data} (cycle starts here)-> ...")
                cycle_detected = True
                break
            print(current.data, end="-> ")
            visited.add(current)
            current = current.next

        if not cycle_detected:
            print("none")

    def find_middle(self, head):
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        return prev

    def find_cycle(self):

        slow = self.head
        fast = self.head
        print(slow, fast)
        while fast and fast.next:
            """find loop"""
            if slow:
                slow = slow.next
                fast = fast.next.next
            if slow == fast:
                print("found cycle")
                print("fast", fast)
                break
        else:
            return None
        print(slow, fast)
        slow = self.head
        while slow != fast:
            """move slow to the start leave fast at the old place, now they step 1 point"""
            if slow:
                slow = slow.next
            if fast and fast.next:
                fast = fast.next
        if slow and fast:
            print(fast.data, slow.data)
        return slow

    def create_cycle(self, position):
        if not self.head:
            return

        cycle_start = None
        current = self.head
        index = 0

        while current.next:
            if index == position:
                cycle_start = current  # Mark cycle start
            current = current.next
            index += 1

        if cycle_start:
            current.next = cycle_start
            print(f"Cycle created at node with value {cycle_start.data}")
        else:
            print("Invalid position: Cycle not created.")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        print("List reversed")
        self.display_full()

    def merge_lists(self, left, right):
        dummy = Node(0)
        tail = dummy

        while left and right:
            if left.data < right.data:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        tail.next = left if left else right
        return dummy.next

    def sort_ll(self, head):
        if not head or not head.next:
            return head

        middle = self.find_middle(head)
        if not middle or not middle.next:
            return head
        right_half = middle.next
        middle.next = None
        left_sorted = self.sort_ll(head)
        right_sorted = self.sort_ll(right_half)
        return self.merge_lists(left_sorted, right_sorted)

    def sort(self):
        self.head = self.sort_ll(self.head)
        self.display_full()


linked_list = Linked_list()
linked_list.append(1)
linked_list.append(4)
linked_list.append(2)
linked_list.append(3)
linked_list.append(5)
linked_list.append(6)
linked_list.append(2)
linked_list.append(12)
linked_list.append(22)
linked_list.append(32)

linked_list.display_full()
linked_list.reverse()
linked_list.sort()


class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
