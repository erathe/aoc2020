lines = [line.strip() for line in open("5.in").readlines()]

def b_search(pattern, rows):
    if len(pattern) == 0:
        return int(rows[0])
    d = pattern.pop(0)
    rows[d] = rows[0] + (rows[1] - rows[0]) // 2
    return b_search(pattern, rows)

def get_id(row, col):
    return row * 8 + col

def get_seat(inp):
    row = b_search([1 if d == "F" else 0 for d in inp[:7]], [0,128])
    col = b_search([1 if d == "L" else 0 for d in inp[7:]], [0, 8])
    return get_id(row, col)

seats = [get_seat(line) for line in lines]
#part 1
print(max(seats))

#part 2
for i in range(min(seats), max(seats) + 1):
    if i-1 in seats and i+1 in seats and i not in seats:
        print(i)
