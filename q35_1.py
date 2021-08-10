# 35. 못생긴 수
n = int(input())

num2_cnt = 2
num3_cnt = 3
num5_cnt = 5

idx_2, idx_3, idx_5 = 0, 0, 0

dp = [0] * n


for i in range(1, n):
    dp[i] = min(num2_cnt, num3_cnt, num5_cnt)
    print(dp[i], idx_2, idx_3, idx_5)

    if dp[i] == num2_cnt:
        idx_2 += 1
        num2_cnt = dp[idx_2] * 2
    if dp[i] == num3_cnt:
        idx_3 += 1
        num3_cnt = dp[idx_3] * 3
    if dp[i] == num5_cnt:
        idx_5 += 1
        num5_cnt = dp[idx_5] * 5

print(dp[n - 1])
