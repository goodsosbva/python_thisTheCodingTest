import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

print(graph)

def get_smallest_nod():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        min_value = distance[i]
        index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
        print("j[0]:",[j[0]])
        print("j[1]:",j[1])
        print(distance[j[0]])
    for i in range(n - 1):
        now = get_smallest_nod()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]
            print("2st)j[0]:", [j[0]])
            print("2st)j[1]:", j[1])
            print(distance[j[0]])

            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

#for i in range(1, n+1):
    #if distance[i] == INF:
        #print("x")
    #else:
        #print(distance[i])
