# 만들 수 없는 금액
n = int(input())
cashs = list(map(int, input().split()))
cashs.sort()

sum = 1
for i in cashs:
    if sum < i:
        break
    sum += 1
print(sum)
