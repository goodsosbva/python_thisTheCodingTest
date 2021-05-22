# 모험가 길드
n = int(input())
fear = list(map(int, input().split()))

fear.sort()
res = 0  # 그륩 수
cnt = 0  # 그륩내 포함된 모험가 수
print(fear)
for i in fear:
    cnt += 1
    if cnt >= i:  # 그륩수가 공포도보다 높다면
        res += 1
        cnt = 0

print(res)

