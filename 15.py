from collections import deque, defaultdict

inp = "0,1,4,13,15,12,16".split(",")
#part 1
#end = 2020
#part 2
end = 30000000
spoken = defaultdict(
    lambda: deque([], 2),
    {int(n): deque([i], 2) for i, n in enumerate(inp, 1)}
)

lastnum = int(inp[-1])
for i in range(len(inp)+1, end+1):
    n = 0 if len(spoken[lastnum]) == 1 else spoken[lastnum][0] - spoken[lastnum][1]
    spoken[n].appendleft(i)
    lastnum = n

print([s for s,q in spoken.items() if end in q])
