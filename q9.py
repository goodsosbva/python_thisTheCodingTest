def sol(s):
    ans = len(s)
    for step in range(1, len(s) // + 1):
        compressed = ""
        prev = s[0:step]
        cnt = 1
        for j in range(step, len(s), step):
            if prev == s[j: j + step]:
                cnt += 1
            else:
                compressed += str(cnt) + prev if cnt >= 2 else prev
                prev = s[j: j + step]
                cnt = 1
        compressed += str(cnt) + prev if cnt >= 2 else prev

        ans = min(ans, len(compressed))

    return ans


strings_ex1 = "aabbaccc"
strings_ex2 = "xababcdcdababcdcd"
sol = sol(strings_ex2)
print(sol)