from collections import defaultdict
lines = [row.strip() for row in open("11.in").readlines()]

dirs = {
        "u": (lambda x,y: (x,y+1)),
        "r": (lambda x,y: (x+1,y)),
        "d": (lambda x,y: (x,y-1)),
        "l": (lambda x,y: (x-1,y)),
        "dur": (lambda x,y: (x+1,y+1)),
        "ddr": (lambda x,y: (x+1,y-1)),
        "ddl": (lambda x,y: (x-1,y-1)),
        "dul": (lambda x,y: (x-1,y+1))
        }

seats = defaultdict(lambda: ".")
for y, row in enumerate(lines):
    for x, val in enumerate(row):
        seats[(x,y)] = val


#part 1
#def get_adj(grid,x,y):
#    return sum(1 for k in dirs.keys() if grid[dirs[k](x,y)] == "#")
#
#def solve(seats):
#    cpseats = seats.copy()
#    changes = 0
#    for y in range(len(lines)):
#        for x in range(len(lines[0])):
#            if cpseats[(x,y)] == "L" and get_adj(cpseats,x,y) == 0:
#                seats[(x,y)] = "#"
#                changes += 1
#            elif cpseats[(x,y)] == "#" and get_adj(cpseats,x,y) >= 4:
#                seats[(x,y)] = "L"
#                changes += 1
#    return changes

def get_adj(grid,x,y):
    adj = 0
    for f in dirs.values():
        dx = x
        dy = y
        while True:
            dx, dy = f(dx,dy)
            if grid[(dx, dy)] == "#":
                adj += 1
                break
            if dx >= len(lines[0]) or dx < 0 or dy < 0 or dy >= len(lines) or grid[(dx,dy)] == "L":
                break
    return adj

def solve(seats):
    cpseats = seats.copy()
    changes = 0
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if cpseats[(x,y)] == "L" and get_adj(cpseats,x,y) == 0:
                seats[(x,y)] = "#"
                changes += 1
            elif cpseats[(x,y)] == "#" and get_adj(cpseats,x,y) >= 5:
                seats[(x,y)] = "L"
                changes += 1
    return changes

while True:
    change = solve(seats)
    if change == 0:
        print("occupied", sum(1 for s in seats.values() if s == "#"))
        break
