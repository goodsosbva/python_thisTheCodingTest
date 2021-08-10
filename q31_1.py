# 31. 금광
test_case = int(input())

for tc in range(test_case):
    n, m = map(int, input().split())
    golds = list(map(int, input().split()))

    dp = []
    idx = 0

    # 일렬로 들어온 값 자르기
    for i in range(n):
        dp.append(golds[idx: idx + m])
        idx += m

    for j in range(1, m):
        for i in range(n):
            # 각가 맨위 와 맨아래는 왼쪽 위에서 오는 값과 왼쪽 아래에서 오는 값이 없으모로 예외 처리
            # 왼쪽 위
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽
            left = dp[i][j - 1]
            # 그 중 최대값 dp 최신화
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    # 마지막 줄에서 가장 큰 값 뽑기
    res = 0
    for i in range(n):
        res = max(res, dp[i][m - 1])

    print(res)


"""
1
3 4
1 3 3 2 2 1 4 1 0 6 4 7
"""