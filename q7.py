strings = input()
mid_len = len(strings) // 2
s1 = 0
s2 = 0

for i in range(mid_len):
    n = int(strings[i])
    s1 += n

for J in range(mid_len, len(strings)):
    n = int(strings[J])
    s2 += n

print(s1, s2)

if s1 == s2:
    print("LUCKY")
else:
    print("READY")