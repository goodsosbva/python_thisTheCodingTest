# 병사 배치하기
n = int(input())
soliders = list(map(int, input().split()))

soliders.reverse()
dp = [1] * n

"""
for i in range(len(soliders)):
    if i == len(soliders) - 1:
        break
    if soliders[i] < soliders[i + 1]:
        dp[i] = max(dp[i], dp[i])
    else:
        cnt += 1


print(cnt)
"""
print(soliders)
for i in range(1, n):
    for j in range(0, i):
        if soliders[j] < soliders[i]:
            dp[i] = max(dp[i], dp[j] + 1)


print(dp)
print(n - max(dp))

"""
7
15 11 4 8 5 2 4
"""