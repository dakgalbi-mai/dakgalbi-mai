def dfs(y, x):
    global cnt
    global check
    check[i][j] = 1
    cnt += 1
    for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
        ny, nx = y+dy, x+dx
        if 0<=ny<n and 0<=nx<n and check[ny][nx] == 0 and ap[ny][nx] == '1':
            dfs(ny, nx)
    return

n = int(input())
ap = []
check = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(n):
    ap.append(list(input()))
ans = 0
cnt_list = []

for i in range(n):
    for j in range(n):
        if check[i][j] == 0 and ap[i][j] == '1':
            ans += 1
            cnt = 0
            dfs(i, j)
            cnt_list.append(cnt)

print(ans)
for i in cnt_list:
    print(i)