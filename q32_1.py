# 32. 정수 삼각형
n = int(input())
triangle = []

for i in range(n):
    triangle.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            diagonal_left = 0
        else:
            diagonal_left = triangle[i - 1][j - 1]

        if i == j:
            diagonal_right = 0
        else:
            diagonal_right = triangle[i - 1][j]

        triangle[i][j] += max(diagonal_right, diagonal_left)


print(max(triangle[n - 1]))


"""
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""


