import re
from collections import deque

lines = [line.strip() for line in open("7.in").readlines()]
tree = {}
for line in lines:
    bag_type, contains = line.split(" contain ")
    bags = re.findall(r'(\d) (\w+ \w+)', contains)
    tree[bag_type[:-5]] = bags

def get_parents(tree, node):
    return [p for p in tree.keys() if any(node in t for t in tree[p])]

def sum_traverse_down(tree, children):
    return sum([int(num) * (1 + sum_traverse_down(tree, tree[node])) for num, node in children])

def traverse_up(tree, node):
    ancestors = set()
    d = deque(get_parents(tree, node))
    while d:
        node = d.popleft()
        if node in ancestors:
            continue;
        ancestors.add(node)
        d.extendleft(get_parents(tree, node))
    return ancestors

#part 1
print(len(traverse_up(tree, "shiny gold")))

#part 2
print(sum_traverse_down(tree, tree["shiny gold"]))
