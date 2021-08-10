# 45. 최종 순위
from collections import deque

test_cast = int(input())

for tc in range(test_cast):
    n = int(input())
    indegree = [0] * (n + 1)
    graph = [[False] * (n + 1) for i in range(n + 1)]

    data = list(map(int, input().split()))

    for i in range(n):
        for j in range(i + 1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1

    print(graph)
    print(indegree)
    e = int(input())

    for _ in range(e):
        a, b = map(int, input().split())

        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    res = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    certain = True
    cycle = False

    for i in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            certain = False
            break

        now = q.popleft()
        res.append(now)

        for i in range(1, n + 1):
            if graph[now][i]:
                indegree[i] -= 1

                if indegree[i] == 0:
                    q.append(i)

    print(res)
    # 사이클이 발생하는 경우(일관성이 없는 경우)
    if cycle:
        print("IMPOSSIBLE")
    # 위상 정렬 결과가 여러 개인 경우
    elif not certain:
        print("?")
    # 위상 정렬을 수행한 결과 출력
    else:
        for i in res:
            print(i, end=' ')
        print()

"""
1
5
5 4 3 2 1
2
2 4
3 4

1
5
1 2 3 4 5
2
2 4
3 4
"""