class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
First=Node(10)
Second=Node(20)
Third=Node(30)
Fourth=Node(40)
Fifth=Node(50)
head=First
head.next=Second
Second.next=Third
Third.next=Fourth
Fourth.next=Fifth
current=head
while current:
    print(current.data, end="---")
    current=current.next  
print("None")