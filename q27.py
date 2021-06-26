n, x = map(int, input().split())
numbers = list(map(int, input().split()))


res = numbers.count(x)
if res == 0:
    print(-1)
else:
    print(res)



"""
7 2
1 1 2 2 2 2 3
"""