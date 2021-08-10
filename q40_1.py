# 40.숨바꼭질
import heapq

n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
start = 1

distance = [999] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    # a -> b 비용 1 이라는 의미
    graph[a].append((b, 1))
    graph[b].append((a, 1))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            #
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

max_node = 0
max_dis = 0
res = []

for i in range(1, n + 1):
    if max_dis < distance[i]:
        max_node = i
        max_dis = distance[i]
        res = [max_node]
    elif max_dis == distance[i]:
        res.append(i)

print(max_node, max_dis, len(res))


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

