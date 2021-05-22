input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

count = 0

directions = [ (-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1) ]

for direction in directions:
    next_row = row + direction[0]
    next_column = column + direction[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        count += 1

print(count)


