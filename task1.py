from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional[Node] = None


class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

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

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            if slow:
                slow = slow.next
            fast = fast.next.next
        if slow:
            print("middle", slow.data)
        else:
            print("The list is empty.")
        return slow.data if slow else None

    def find_cycle(self):

        slow = self.head
        fast = self.head
        print(slow, fast)
        while fast and fast.next:
            """find loop"""
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


linked_list = Linked_list()
linked_list.append(1)
linked_list.append(4)
linked_list.append(2)
linked_list.append(3)
linked_list.append(5)
linked_list.append(6)
linked_list.append(2)
linked_list.append(4)
linked_list.append(1)

if (
    linked_list.head
    and linked_list.head.next
    and linked_list.head.next.next
    and linked_list.head.next.next.next
):
    linked_list.head.next.next.next.next = linked_list.head.next
loop = linked_list.find_cycle()

linked_list.display_full()


class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
