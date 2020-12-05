lines = [line.strip() for line in open("5.in").readlines()]

def b_search(pattern, rows, key):
    if len(pattern) == 0:
        return int(rows[0])
    d = pattern.pop(0)
    nextFirst = rows[0] if d == key else rows[len(rows)//2]
    nextLast = rows[len(rows)//2] if d == key else rows[len(rows)-1] + 1
    return b_search(pattern, list(range(nextFirst, nextLast)), key)

seats = {b_search(list(seat[0:7]), list(range(0,128)), "F")*8 + b_search(list(seat[7:]), list(range(0,9)), "L") for seat in lines}
#part 1
print(max(seats))

#part 2
for i in range(min(seats), max(seats) + 1):
    if i-1 in seats and i+1 in seats and i not in seats:
        print(i)
