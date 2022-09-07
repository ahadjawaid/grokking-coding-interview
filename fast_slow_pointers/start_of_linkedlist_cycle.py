class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


def find_cycle_start(head):
    visited = set()

    currNode = head
    while currNode:
        if currNode in visited:
            return currNode
        else:
            visited.add(currNode)
            currNode = currNode.next


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

head.next.next.next.next.next.next = head.next.next
print("LinkedList cycle start: " + str(find_cycle_start(head).value))

head.next.next.next.next.next.next = head.next.next.next
print("LinkedList cycle start: " + str(find_cycle_start(head).value))

head.next.next.next.next.next.next = head
print("LinkedList cycle start: " + str(find_cycle_start(head).value))
