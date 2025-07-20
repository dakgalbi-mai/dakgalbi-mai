def f(cur):
    global ans
    if cur == 0:
        ans += 1
        return
    if cur <= -1:
        return
    f(cur-2)
    f(cur-1)

n = int(input())
ans = 0
f(n)
print(ans)