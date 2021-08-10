# 행성 터널

def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())

parent = [0] * (n + 1)

for i in range(n):
    parent[i] = i

data = []
x, y, z = [], [], []

for i in range(1, n + 1):
    a, b, c = list(map(int, input().split()))
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort()
y.sort()
z.sort()

# 비용 처리 해주는 곳 ( cost, a, b ) 꼴
for i in range(n - 1):
    data.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    data.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    data.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))


data.sort()
res = 0

for d in data:
    cost, a, b = d
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res += cost

print(res)



