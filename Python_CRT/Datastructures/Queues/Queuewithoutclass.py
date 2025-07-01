from collections import deque
stack=deque()
stack.append('A')
stack.append('B')
stack.append('C')
print("stack after enqueuing:",stack)
first=stack.popleft()
print("Destackd element:",first)
print("stack after Dequeuing:",stack)
if not stack:
    print("stack is empty")
else:
    print("stack is not empty")
print("Front element:",stack[0])
print("--------------------------")

# Stack
from collections import deque
stack=deque()
stack.append('A')
stack.append('B')
stack.append('C')
print("stack after enqueuing:",stack)
top=stack.popleft()
print("Destackd element:",top)
print("stack after Dequeuing:",stack)
if not stack:
    print("stack is empty")
else:
    print("stack is not empty")
print("Front element:",stack[0])
