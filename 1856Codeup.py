def f(cur):
    global ans
    if cur == n:
        ans += 1
        return
    if cur > n:
        return
    f(cur+1)
    f(cur+2)
    f(cur+3)

n = int(input())
ans = 0
f(0)
print(ans)