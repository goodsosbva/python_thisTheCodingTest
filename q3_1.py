strings_n = input()

cnt0 = 0
cnt1 = 0

for i in range(len(strings_n) - 1):
    if strings_n[i] == "0":
        cnt1 += 1
        if strings_n[i] != strings_n[i + 1]:
            if strings_n[i + 1] == "0":
                cnt1 += 1
    else:
        cnt0 += 1
        if strings_n[i] != strings_n[i + 1]:
            if strings_n[i + 1] == "1":
                cnt0 += 1

print(min(cnt0, cnt1))
print(cnt0, cnt1)