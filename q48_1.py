n, m, k = map(int, input().split())

# 모든 상어의 위치와 방향 정보를 포함하는 2차원 리스트
sharks_pos = []
for i in range(n):
    sharks_pos.append(list(map(int, input().split())))

# 모든 상어의 현재 방향 정보
sharks_direction = list(map(int, input().split()))

# 각 위치마다 [특정 냄새의 상어 번호, 특정 냄새의 남은 시간]을 저장하는 2차원 리스트
smell = [[[0, 0]] * n for _ in range(n)]

# 각 상어의 회전 우선순위 정보
sharks_priority = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        sharks_priority[i].append(list(map(int, input().split())))

# 특정 위치에서 이동 가능한 4가지 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 모든 냄새 정보를 업데이트
def update_smell():
    # 각 위치를 하나씩 확인하며
    for i in range(n):
        for j in range(n):
            # 냄새가 존재하는 경우, 시간을 1만큼 감소시키기
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            # 상어가 존재하는 해당 위치의 냄새를 k로 설정
            if sharks_pos[i][j] != 0:
                smell[i][j] = [sharks_pos[i][j], k]


# 모든 상어를 이동시키는 함수
def move():
    # 이동 결과를 담기 위한 임시 결과 테이블 초기화
    new_sharks_pos = [[0] * n for _ in range(n)]
    # 각 위치를 하나씩 확인하며
    for x in range(n):
        for y in range(n):
            # 상어가 존재하는 경우
            if sharks_pos[x][y] != 0:
                direction = sharks_direction[sharks_pos[x][y] - 1]  # 현재 상어의 방향
                found = False
                # 일단 냄새가 존재하지 않는 곳이 있는지 확인
                for idx in range(4):
                    nx = x + dx[sharks_priority[sharks_pos[x][y] - 1][direction - 1][idx] - 1]
                    ny = y + dy[sharks_priority[sharks_pos[x][y] - 1][direction - 1][idx] - 1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][1] == 0:  # 냄새가 존재하지 않는 곳이면
                            # 해당 상어의 방향 이동시키기
                            sharks_direction[sharks_pos[x][y] - 1] = sharks_priority[sharks_pos[x][y] - 1][direction - 1][idx]
                            # 상어 이동시키기 (만약 이미 다른 상어가 있다면 번호가 낮은 것이 들어가도록)
                            if new_sharks_pos[nx][ny] == 0:
                                new_sharks_pos[nx][ny] = sharks_pos[x][y]
                            else:
                                new_sharks_pos[nx][ny] = min(new_sharks_pos[nx][ny], sharks_pos[x][y])
                            found = True
                            break
                if found:
                    continue
                # 주변에 모두 냄새가 남아 있다면, 자신의 냄새가 있는 곳으로 이동
                for idx in range(4):
                    nx = x + dx[sharks_priority[sharks_pos[x][y] - 1][direction - 1][idx] - 1]
                    ny = y + dy[sharks_priority[sharks_pos[x][y] - 1][direction - 1][idx] - 1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][0] == sharks_pos[x][y]:  # 자신의 냄새가 있는 곳이면
                            # 해당 상어의 방향 이동시키기
                            sharks_direction[sharks_pos[x][y] - 1] = sharks_priority[sharks_pos[x][y] - 1][direction - 1][idx]
                            # 상어 이동시키기
                            new_sharks_pos[nx][ny] = sharks_pos[x][y]
                            break
    return new_sharks_pos


time = 0
while True:
    update_smell()  # 모든 위치의 냄새를 업데이트
    new_array = move()  # 모든 상어를 이동시키기
    sharks_pos = new_array  # 맵 업데이트
    time += 1  # 시간 증가

    # 1번 상어만 남았는지 체크
    check = True
    for i in range(n):
        for j in range(n):
            if sharks_pos[i][j] > 1:
                check = False
    if check:
        print(time)
        break

    # 1000초가 지날 때까지 끝나지 않았다면
    if time >= 1000:
        print(-1)
        break
