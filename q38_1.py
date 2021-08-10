# 38. 정확한 순위
n, m = map(int, input().split())

reports = [[999] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            reports[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    reports[a][b] = 1

for k in range(1, n + 1):
    # print(reports)
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            reports[a][b] = min(reports[a][b], reports[a][k] + reports[k][b])

res = 0

for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        if reports[i][j] != 999 or reports[j][i] != 999:
            cnt += 1
    if cnt == n:
        res += 1


print(reports)
print(res)
