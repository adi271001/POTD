def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]
 
def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    parent[y] = x
 
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
edges = []
for i in range(m):
    a, b = map(int, input().split())
    edges.append((a, b))
 
res = 0
for a, b in edges:
    if find(a) == find(b):
        res += 1
        continue
    union(a, b)
print(res)
