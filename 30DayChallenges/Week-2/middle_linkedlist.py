
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def middleNode(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

print(middleNode(node1).value)

