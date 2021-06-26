n = int(input())
arrays = list(map(int, input().split()))

for idx, value in enumerate(arrays):
    if idx == value:
        print(idx)
        break


"""
5
-15 -6 1 3 7
"""