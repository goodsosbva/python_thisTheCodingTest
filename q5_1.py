# 볼링공 고르기_2
n, m = map(int, input().split())
weights = list(map(int, input().split()))

# 1~10까지 담을 리스트
array = [0] * 11
for x in weights:
    # 각 무게에 해당하는 개수 카운트
    array[x] += 1

res = 0
for i in range(1, m + 1):
    n -= array[i]
    res += array[i] * n

print(res)