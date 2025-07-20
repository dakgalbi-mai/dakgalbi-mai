v, e = map(int, input().split())
node = [[] for _ in range(10)]
for i in range(e):
    v1, v2 = map(int, input().split())
    node[v1].append(v2)

for i in range(10):
    for j in range(len(node[i])):
        print(i,node[i][j])
