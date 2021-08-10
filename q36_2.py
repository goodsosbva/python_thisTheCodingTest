# 36. 편집 거리

def edit_distance(str1, str2):
    n = len(str1)
    m = len(str2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, m + 1):
        dp[0][j] = j

    for i in range(n + 1):
        for j in range(m + 1):
            # 같은 경우
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # 틀릴 경우(+1) + 왼쪽위, 왼쪽, 위중 작은 값 최신화
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])

    return dp[n][m]


str1 = input()
str2 = input()

print(edit_distance(str1, str2))