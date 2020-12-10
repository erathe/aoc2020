from collections import defaultdict
lines = [int(line.strip()) for line in open("10.in").readlines()] + [0]
lines.append(max(lines) + 3)
lines.sort()
lines.reverse()

diffs = defaultdict(lambda: 0)
for i, l in enumerate(lines):
    if l == 0:
        break
    diffs[l-lines[i+1]] += 1

#part 1
print(diffs[3] * diffs[1])
#part 2
adjList = dict()
for l in lines:
    adjList[l] = [x for x in lines if x-l <=3 and x > l]

paths = defaultdict(lambda: 0)
def dfs(s, e, adj):
    if s == e:
        return 1
    else:
        if not paths[s]:
            paths[s] = sum(dfs(c, e, adj) for c in adj[s])
        return paths[s]
print(dfs(min(lines), max(lines), adjList))
