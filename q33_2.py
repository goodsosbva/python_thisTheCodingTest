# 33. 퇴사

n = int(input())
counsel_table = []

for i in range(n):
    counsel_table.append(list(map(int, input().split())))

dp = [0] * (n + 1)

print(counsel_table)
max_val = 0
time = 0

# 거꾸로 for문을 돌면 엄청 쉬워짐..
for i in range(n - 1, -1, -1):
    time = counsel_table[i][0] + i
    print(dp)
    if time <= n:
        dp[i] = max(counsel_table[i][1] + dp[time], max_val)
        max_val = dp[i]
    else:
        dp[i] = max_val

print(max_val)

"""
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
"""

