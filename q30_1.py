# 30. 가사 검색
from bisect import bisect_left, bisect_right

array = [[] for _ in range(10001)]
reverse_array = [[] for _ in range(100001)]


def solution(words, queries):
    ans = []
    for word in words:
        array[len(word)].append(word)
        reverse_array[len(word)].append(word[::-1])

    for i in range(100):
        array[i].sort()
        reverse_array[i].sort()
        # print(i, array)
        # print(reverse_array)

    for q in queries:
        if q[0] != '?':
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
            print(res)
        else:
            res = count_by_range(reverse_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))

        ans.append(res)
    return ans


def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)

    print(right_index, left_index, array, right_value, left_value)

    return right_index - left_index


queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
sol = solution(words, queries)
print(sol)
