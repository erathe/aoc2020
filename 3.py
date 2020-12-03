import functools
import operator
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
inp = [line.strip() for line in open("3.in").readlines()]

def get_trees(slope):
    trees = x = y = 0
    dx, dy = slope
    while y < len(inp):
        if inp[y][x % len(inp[y])] == '#':
            trees += 1
        x += dx
        y += dy
    return trees

print(functools.reduce(operator.mul, [get_trees(slope) for slope in slopes]))
