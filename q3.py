# 문자열 뒤집기
strings = input()

cnt0 = 0
cnt1 = 0

if strings[0] == "0":
    cnt1 += 1
else:
    cnt0 += 1


for i in range(len(strings) - 1):
    if strings[i] != strings[i + 1]:
        if strings[i + 1] == "0":
            cnt1 += 1
        else:
            cnt0 += 1

print(min(cnt0, cnt1))
print(cnt0, cnt1)