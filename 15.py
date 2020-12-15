from collections import deque, defaultdict

inp = "0,1,4,13,15,12,16".split(",")
end = 30000000
spoken = defaultdict(lambda: deque([], 2))

for i, n in enumerate(inp):
    spoken[int(n)].appendleft(i+1)

lastnum = int(inp[-1])
for i in range(len(inp)+1, end+1):
    if len(spoken[lastnum]) == 1:
        spoken[0].appendleft(i)
        lastnum = 0
    else:
        n = spoken[lastnum][0] - spoken[lastnum][1]
        spoken[n].appendleft(i)
        lastnum = n

print([s for s,q in spoken.items() if end in q])
