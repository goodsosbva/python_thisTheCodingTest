# 볼링공 고르기
n, m = map(int, input().split())
weights = list(map(int, input().split()))

weights.sort()
association = []

for i in weights:
    for j in range(len(weights)):
        if i != weights[j]:
            if (weights[j], i) not in association:
                association.append((i, weights[j]))

print(len(association))
