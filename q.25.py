from collections import deque

n = int(input())
stages = list(map(int, input().split()))

data = []
# q.append(stages)
stages.sort()
user_summary = len(stages)

for i in range(1, n + 1):
    user_number = stages.count(i)
    print(user_number)
    if user_summary == 0:
        fail_number = 0
    else:
        fail_number = user_number / user_summary

    data.append((i, fail_number))
    user_summary = user_summary - user_number

data.sort(key=lambda x: -x[1])
res = []
for i in data:
    res.append(i[0])

print(res)

"""
5
2 1 2 6 2 4 3 3

res =
3 4 2 1 5
"""
