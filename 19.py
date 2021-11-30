import re
from functools import lru_cache
rules, codes = [line.strip() for line in open("19.in").read().split("\n\n")]
rulebook = dict()
l = ""
for rule in rules.split("\n"):
    key, val = rule.split(": ")
    if val in ["\"a\"", "\"b\""]:
        rulebook[key] = re.match(r"\"(a|b)\"", val).groups()[0]
    else:
        rulebook[key] = [s.split(" ") for s in val.split(" | ")]

tree = dict()
@lru_cache(maxsize=10000)
def dfs(node):
    if rulebook[node] in ["a", "b"]:
        tree[node] = rulebook[node]
        return tree[node]
    for r in rulebook[node]:
        tree["".join(r)] = [dfs(n) for n in r]
    return tree

f = dfs("0")
print(f)
