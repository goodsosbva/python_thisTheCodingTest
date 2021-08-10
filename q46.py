# 46. 아기 상어
from collections import deque

n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n_x, n_y = 0, 0
now_size = 2

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            n_x, n_y = i, j
            graph[n_x][n_y] = 0


def bfs():
    dist = [[-1] * n for _ in range(n)]
    q = deque()
    q.append(n_x, n_y)

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 and nx >= n or ny >= n:
                continue
            if graph[nx][ny] <= now_size and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    return dist


def eating(dist):
    x, y = 0, 0
    min_dist = 9999
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= graph[i][j] < now_size:
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == 9999:
        return None
    else:
        return x, y, min_dist


res = 0
ate = 0

while True:
    val = eating(bfs())

    if val == None:
        print(res)
        break
    else:
        n_x, n_y = val[0], val[1]
        res += val[2]
        graph[n_x][n_y] = 0
        ate += 1

        if ate >= now_size:
            now_size += 1
            ate = 0


