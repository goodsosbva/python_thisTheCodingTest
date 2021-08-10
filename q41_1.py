# 41. 여행 계획

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


n, m = map(int, input().split())
parent = [0] * (n + 1)
# graph = []

for i in range(1, n + 1):
    parent[i] = i

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:  # 집합일 경우
            union_parent(parent, i + 1, j + 1)
            print(parent)


plans = list(map(int, input().split()))

res = True

for i in range(m - 1):
    if find_parent(parent, plans[i]) != find_parent(parent, plans[i + 1]):
        res = False

if res:
    print("Y")
else:
    print("N")




