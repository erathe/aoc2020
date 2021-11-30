from collections import defaultdict
from itertools import product, permutations

lines = [line.strip() for line in open("17.in").readlines()]
moves = [x for x in product([-1, 0, 1], repeat=4)]
grid = defaultdict(lambda: ".")

def get_neighbours(x, y, z, w, active):
    return sum([1 for dx, dy, dz, dw in moves if (x+dx,y+dy,z+dz,w+dw) in active and (dx,dy,dz,dw) != (0,0,0,0)])

#misuse defaultdict to grow the grid by one in all directions
def grow(grid):
    c = grid.copy()
    for dx,dy,dz,dw in moves:
        for x,y,z,w in c:
            grid[(x+dx,y+dy,z+dz,w+dw)]

#initialise grid
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        for z, w in product([-1,0,1], repeat=2):
            grid[(x,y,z,w)] = "."
        grid[(x,y,0,0)] = char

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
