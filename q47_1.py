# 47. 청소년 상어

# 1. 4 * 4 격자를 만들자
import copy
array = [[None] * 4 for _ in range(4)]

# 2. 격자에다가 데이터를 입력 받자
for i in range(4):
    data = list(map(int, input().split()))
    # 3. 조건에 맞게 [물고기의 번허, 방향] 입력 받은 데이터에 따라 저장해주자
    for j in range(4):
        array[i][j] = [data[j * 2], data[j * 2 + 1] - 1]

# 4. 이동할 수 있는 8가지 방향을 설정해주자
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
result = 0


# 6. 5-2 물고기 이동 함수를 만들어보자
def move_all_fishes(array, now_x, now_y):
    # 1번 ~ 16번 확인
    # 물고기를 찾는 함수를 만들어보자 -> # 7
    for i in range(1, 17):
        positon = find_fish(array, i)
        if positon != None:
            x, y = positon[0], positon[1]
            direction = array[x][y][1]
            # 해당 물고기를 반시계 방향으로 회전하면서 이동 가능 여부 체크
            for j in range(8):
                # 오른쪽 회전은 여기서 이루어지지 않는다
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0 <= nx and nx < 4 and 0 <= ny and ny < 4:
                    if not (nx == now_x and ny == now_y):
                        array[x][y][1] = direction
                        # 이동
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                        break
                # 회전은 여기서 적용
                # 회전하는 함수를 만들어주자 -> # 8
                direction = turn_left(direction)


# 7. 물고기를 찾는 함수
def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i, j)
    return None


# 8. 회전하는 함수
def turn_left(direction):
    return (direction + 1) % 8


# 9. 상어가 현재 위치에서 먹이를 먹을 수 있는지 없는지 체크하는 함수
def get_possible_positions(array, now_x, now_y):
    positions = []
    direction = array[now_x][now_y][1]
    # 상어가 가지고 있는 이동 방향으로 계속 움직여서 먹이 확인
    # 틀의 크기가는 4이므로 4를 넘을 수 없으므로 range의 크기는 4
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        # 밤위를 벗어나는지 체크
        if 0 <= now_x and now_x < 4 and 0 <= now_y and now_y < 4:
            # 물고기가 존재
            if array[now_x][now_y] != -1:
                positions.append((now_x, now_y))
    return positions


# 5. main 부분 작성
def dfs(array, now_x, now_y, total):
    # 5-1. 상어가 현위치에 물고기를 먹는다
    global result
    array = copy.deepcopy(array)
    total += array[now_x][now_y][0]  # 번호 더하기
    array[now_x][now_y][0] = -1  # 먹음 표시
    # 5-2. 물고기 이동
    move_all_fishes(array, now_x, now_y)
    # 5-3. 상어 이동 (먹이를 먹을 수 있는 위치로 이동. 즉 조건에 따라 먹을 수 있을 때 이동할 수 있으므로 먹을 수 있는지 확인 하는 함수를 만들자
    positions = get_possible_positions(array, now_x, now_y)
    # 5-4. 이동할 수 있는 위치가 없을 경우
    if len(positions) == 0:
        result = max(result, total)
        return
    # 5-5. 아니라면 재귀로 계속 수행
    for next_x, next_y in positions:
        dfs(array, next_x, next_y, total)


dfs(array, 0, 0, 0)
print(result)





