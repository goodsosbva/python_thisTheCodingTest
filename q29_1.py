# 29. 공유기 설치
n, c = map(int, input().split())

routers = []

for i in range(n):
    routers.append(int(input()))

routers.sort()

max_len = routers[-1] - routers[0]
min_len = routers[1] - routers[0]
res = 0

while max_len >= min_len:
    mini_distance = (max_len + min_len) // 2
    val = routers[0]
    cnt = 1
    print("hi", max_len, min_len, mini_distance)
    for i in range(1, n):
        if routers[i] - val >= mini_distance:
            cnt += 1
            val = routers[i]

    if cnt >= c:
        min_len = mini_distance + 1
        res = mini_distance
        print("if", min_len)
    else:
        max_len = mini_distance - 1
        print("else", max_len)

print(res)
