from collections import deque
arr = list(input().split())
print(arr)
stk = deque()
for i in arr:
    stk.appendleft(i)

while len(stk) != 0:
    print(stk.popleft())