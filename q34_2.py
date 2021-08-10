# 34. 병사 배치하기

n = int(input())
soldiers = list(map(int, input().split()))

prev = soldiers[0]
cnt = 0

for i in range(1, len(soldiers)):
    # print(prev, soldiers[i])
    if prev > soldiers[i]:
        prev = soldiers[i]
    else:
        prev = soldiers[i - 2]
        cnt += 1

print(cnt)