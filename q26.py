from collections import deque
import heapq

n = int(input())
numbers = deque()

for i in range(n):
    num = int(input())
    numbers.append(num)

# 디큐는 sort를 지원하지 않아서 결국에는 틀림..
sum = 0
while len(numbers) != 1:
    left = numbers.popleft()
    right = numbers.popleft()
    # print(left, right)
    summary = left + right
    numbers.append(summary)
    sum += summary

print(sum)


"""
3
10
20
40
"""
