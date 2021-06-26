# 편집 거리
a = input()
b = input()
if len(a) >= len(b):
    real_1 = a
    real_2 = b
    max_val = len(a)
else:
    real_1 = b
    real_2 = a
    max_val = len(b)
gap = 0
string_gab = 0
not_same = 0

if len(a) != len(b):
    gap += abs(len(a) - len(b))
    string_gab = abs(len(a) - len(b))
    # print(gap)
    str_same = 1

else:
    str_same = 0

for i in real_1:
    if i not in real_2:
        not_same += 1


print(gap + not_same - str_same)


"""
ex1 =
cat
cut
ex2 =
sunday
saturday
"""