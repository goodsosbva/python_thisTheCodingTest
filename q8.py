strings = input()

data = []
summary = 0

for i in strings:
    if i.isalpha():
        data.append(i)
    else:
        summary += int(i)

data.sort()
data.append(str(summary))
print(data)
print(''.join(data))