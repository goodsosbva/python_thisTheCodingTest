import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = int(1e9)
start = 1
graph = [[] * (n + 1) for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 0 , start = 초기 비용, 초기 위치
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

max_node = 0
max_distance = 0
res = []

for i in range(1, n + 1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        res = [max_node]
    elif max_distance == distance[i]:
        res.append(i)


print(max_node, max_distance, len(res))


"""
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
"""