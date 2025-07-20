def f(a,b):
    if a > n:
        if b == k: ans += 1
        return
    f(a+1, b)
    f(a+1, b+1)
n, k = map(int, input().split())
ans =0
f(1, 0)
print(ans)