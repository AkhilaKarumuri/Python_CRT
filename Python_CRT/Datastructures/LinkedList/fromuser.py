"""WAPP to create a linked list of size n take the value of 'n' as user's input """
class Node:
    def init(self, data):
        self.data = data
        self.next = None
n = int(input("Enter size of linked list: "))
val = int(input("Enter value for node 1: "))
head = Node(val)
temp = head
for i in range(2, n+1):
    val = int(input(f"Enter value for node {i}: "))
    temp.next = Node(val)
    temp = temp.next
temp = head
while temp:
    print(temp.data, end=" ")
    temp = temp.next