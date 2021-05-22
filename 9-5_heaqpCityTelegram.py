import heapq
import sys

input = sys.stdin.readline
IMF = int(1e9)

n, m, start = map(int, input().split())
graph = [[] for i in range(n + 1)]
distance = [IMF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    print(graph)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    k = 0
    while q:
        k = k + 1
        print("%d 번째 while문" % (k))
        # print(q)
        dist, now = heapq.heappop(q)

        # print("q:",q)
        print("dist:", dist)
        print("now:", now)
        print("distance:", distance)
        if distance[now] < dist:
            continue
        for i in graph[now]:

            cost = dist + i[1]  # i[1] : 비용
            print("cost:", cost)

            # print("distane[%d[0]]:",i,distance[i[0]])

            if cost < distance[i[0]]:  # i[0] : 목적지 노드
                distance[i[0]] = cost
                print("distance:", distance[i[0]])

                heapq.heappush(q, (cost, i[0]))
                print("q:", q)


dijkstra(start)

count = 0

max_distance = 0
for d in distance:
    if d != IMF:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance)
# print("결과 distance:", distance)
# print(graph)


"""
3 2 1
1 2 4
1 3 2

3 2 1
1 2 6
1 3 2
"""
