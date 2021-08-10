# 화성 탐사
import heapq

test_case = int(input())
INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(test_case):
    n = int(input())
    costs = []
    dis = [[INF] * n for _ in range(n)]

    for _ in range(n):
        costs.append(list(map(int, input().split())))

    x, y = 0, 0
    q = [(costs[x][y], x, y)]
    dis[x][y] = costs[x][y]

    while q:
        # print(dis)
        dist, x, y = heapq.heappop(q)
        if dis[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                now_cost = dist + costs[nx][ny]
                if now_cost < dis[nx][ny]:
                    dis[nx][ny] = now_cost
                    heapq.heappush(q, (now_cost, nx, ny))

    print(dis)
    print(dis[n - 1][n - 1])



