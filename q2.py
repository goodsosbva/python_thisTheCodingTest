# 곱하기 혹은 더하기
n = input()

ch_num = int(n[0])

for i in range(1, len(n)):
    num = int(n[i])

    if num <= 1 or ch_num <= 1:
        ch_num += num
    else:
        ch_num *= num

print(ch_num)


