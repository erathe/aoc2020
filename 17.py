from collections import defaultdict
from itertools import permutations

lines = [line.strip() for line in open("17.in").readlines()]
n = set(permutations([1,1,1,1,0,0,0,0,-1,-1,-1,-1], 4))
n.remove((0,0,0,0))
grid = defaultdict(lambda: ".")

def get_neighbours(x, y, z, w, active):
    return sum([1 for dx, dy, dz, dw in n if (x+dx,y+dy,z+dz,w+dw) in active])

#misuse defaultdict to grow the grid by one in all directions
def grow(grid):
    c = grid.copy()
    for dx,dy,dz,dw in n:
        for x,y,z,w in c:
            grid[(x+dx,y+dy,z+dz,w+dw)]

#initialise grid
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        grid[(x,y,0,0)] = char
        grid[(x,y,-1,0)] = "."
        grid[(x,y,1,0)] = "."
        grid[(x,y,0,1)] = "."
        grid[(x,y,-1,1)] = "."
        grid[(x,y,1,1)] = "."
        grid[(x,y,0,-1)] = "."
        grid[(x,y,-1,-1)] = "."
        grid[(x,y,1,-1)] = "."

for i in range(6):
    grow(grid)
    active = {c for c, v in grid.items() if v == "#"}
    for (x, y, z, w), v in grid.items():
        neighbours = get_neighbours(x,y,z,w,active)
        if v == "#" and neighbours not in [2,3]:
            grid[(x,y,z,w)] = "."
        elif v == "." and neighbours == 3:
            grid[(x,y,z,w)] = "#"

#part 1 and 2
print(sum(1 for g in grid.values() if g == "#"))
