def f(a, b, c):
    global ans
    if a > n:
        if b == k:
            ans += 1
        return
    f(a+1, b, 0)
    if c == 0: f(a+1, b+1, 1)

n, k = map(int, input().split())
ans = 0
f(1, 0, 0)
print(ans)