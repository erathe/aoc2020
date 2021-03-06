from collections import defaultdict
from functools import lru_cache
lines = [int(line.strip()) for line in open("10.in").readlines()]
lines = [0] + sorted(lines) + [max(lines) + 3]

diffs = defaultdict(lambda: 0)
for a, b in zip(lines, lines[1:]):
    diffs[b-a] += 1
#part 1
print(diffs[3] * diffs[1])

#part 2
adjList = dict()
for l in lines:
    adjList[l] = [x for x in lines if x-l <=3 and x > l]

@lru_cache(maxsize=len(lines))
def dfs(s, e):
    if s == e:
        return 1
    else:
        return sum(dfs(c, e) for c in adjList[s])

print(dfs(min(lines), max(lines)))

#part 2 alternative
stairs = defaultdict(lambda: 0)
stairs[0] = 1
for n in lines[1:]:
    stairs[n] = stairs[n-1] + stairs[n-2] + stairs[n-3]

print(stairs[lines[-1]])
