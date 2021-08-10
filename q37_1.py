# 37. 플로이드
cities = int(input())
lines = int(input())

bus_cost = [[999] * (cities + 1) for _ in range(cities + 1)]

for a in range(1, cities + 1):
    for b in range(1, cities + 1):
        if a == b:
            bus_cost[a][b] = 0


for _ in range(lines):
    a, b, c = list(map(int, input().split()))
    if c < bus_cost[a][b]: # 처음 최신화 되는것
        bus_cost[a][b] = c

# 플로이드 워셜 알고리즘
for k in range(1, cities + 1):
    for a in range(1, cities + 1):
        for b in range(1, cities + 1):
            bus_cost[a][b] = min(bus_cost[a][b], bus_cost[a][k] + bus_cost[k][b])


for a in range(1, cities + 1):
    for b in range(1, cities + 1):
        print(bus_cost[a][b], end=" ")
    print()


"""
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
"""




