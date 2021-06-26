n = int(input())
works = []
dp = [0] * (n + 1)

for _ in range(n):
    t, p = map(int, input().split())
    works.append([t, p])

# print(works)
i = 0
max_val = 0
time = 0
tmp = 0
idx = works[0][0]
#for i in range(n):
while i < n:
    # print(idx)
    time = time - tmp
    time = time + works[i][0]
    tmp = time
    if idx + time > n:
        break
    if time <= n:
        max_val = max_val + works[i][1]
        i += time
        # print("i", i, max_val)
    else:
        time = time - works[i][0]
        i -= time
        continue
    idx += 1
print(max_val)

# 실패한 코딩,, 재귀로도 복잡하고 정방향은 아닌거같다...
