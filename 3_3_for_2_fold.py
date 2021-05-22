n, m = map(int, input().split())
i = 0
result = 0

for i in range(n):
    data = list(map(int, input().split()))

    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
        #print(min_value)

    i = i + 1
    print("몇번째?:", i)
    result = max(result, min_value)

print("max:" ,result)