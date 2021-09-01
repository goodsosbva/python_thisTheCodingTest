# 48. 어른 상어
n, m, k = map(int, input().split())
sharks_pos = []

for i in range(n):
    sharks_pos.append(list(map(int, input().split())))
sharks_direction = list(map(int, input().split()))

sharks_priority = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        sharks_priority[i].append(list(map(int, input().split())))
smell = [[[0, 0]] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 1_1
def update_smell():
    for x in range(n):
        for y in range(n):
            if smell[x][y][1] > 0:
                smell[x][y][1] -= 1

            if sharks_pos[x][y] != 0:
                smell[x][y] = [sharks_pos[x][y], k]  # smell = [ 상위 위치, 냄새 유효 시간 ]


# 2_2
def sharks_move():
    # 2-1.
    new_sharks_pos = [[0] * n for _ in range(n)]
    # 2-2.
    for x in range(n):
        for y in range(n):
            if sharks_pos[x][y] != 0:  # 상어가 있다면
                direction = sharks_direction[sharks_pos[x][y] - 1]
                found = False
                # 2-3
                for idx in range(4):
                    nx = x + dx[sharks_priority[sharks_pos[x][y] - 1][direction - 1][idx] - 1]
                    ny = y + dy[sharks_priority[sharks_pos[x][y] - 1][direction - 1][idx] - 1]

                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][1] == 0:
                            # 2_3_1
                            sharks_direction[sharks_pos[x][y] - 1] = sharks_priority[sharks_pos[x][y] - 1][direction - 1][idx]
                            # 2_3_2
                            if new_sharks_pos[nx][ny] == 0:
                                new_sharks_pos[nx][ny] = sharks_pos[x][y]
                            else:
                                new_sharks_pos[nx][ny] = min(new_sharks_pos[nx][ny], sharks_pos[x][y])
                            found = True
                            break
                if found:
                    continue
                # 2-4
                for idx in range(4):
                    nx = x + dx[sharks_priority[sharks_pos[x][y] - 1][direction - 1][idx] - 1]
                    ny = y + dy[sharks_priority[sharks_pos[x][y] - 1][direction - 1][idx] - 1]

                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][0] == sharks_pos[x][y]:
                            # 2_4_1
                            sharks_direction[sharks_pos[x][y] - 1] = sharks_priority[sharks_pos[x][y] - 1][direction - 1][idx]
                            # 2_4_2
                            new_sharks_pos[nx][ny] = sharks_pos[x][y]
                            break
    return new_sharks_pos


time = 0
# solution 부분
while True:
    # 1. 냄새를 업데이트한다.
    update_smell()
    # 2. 상어를 움직인다.
    new_shark_pos = sharks_move()
    sharks_pos = new_shark_pos
    time += 1

    check = True
    # 3. 상어가 하나만 남았는지 체크
    for i in range(n):
        for j in range(n):
            if new_shark_pos[i][j] > 1:
                check = False

    # no
    if not check:
        continue
    # yes
    else:
        print(time)
        break
    # 제약 조건
    if time > 1000:
        print(-1)
        break



"""
5 4 4
0 0 0 0 3
0 2 0 0 0
1 0 0 0 4
0 0 0 0 0
0 0 0 0 0
4 4 3 1
2 3 1 4
4 1 2 3
3 4 2 1
4 3 1 2
2 4 3 1
2 1 3 4
3 4 1 2
4 1 2 3
4 3 2 1
1 4 3 2
1 3 2 4
3 2 1 4
3 4 1 2
3 2 4 1
1 4 2 3
1 4 2 3
"""

