class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def has_cycle(root):
    s, f = root, root

    while s and f:
        s = s.next
        if f.next:
            f = f.next.next

        if s == f:
            return True

    return False


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
print("LinkedList has cycle: " + str(has_cycle(head)))

head.next.next.next.next.next.next = head.next.next
print("LinkedList has cycle: " + str(has_cycle(head)))

head.next.next.next.next.next.next = head.next.next.next
print("LinkedList has cycle: " + str(has_cycle(head)))
