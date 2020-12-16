import re
lines = [line for line in open("16.in").read().split("\n\n")]

rules, tick, other = [l.strip() for l in lines]

#part 1, Doesnt work at all for part 2 (:
#reuse the legal set because i cba rewriting it
legal = set()
for r in rules.split("\n"):
    s1, e1, s2, e2 = [int(x) for x in re.findall(r"(\d+)-(\d+) or (\d+)-(\d+)", r)[0]]
    legal.update(list(range(s1,e1+1)) + list(range(s2,e2+1)))

#should be using this to generate valid
rule = dict()
for r in rules.split("\n"):
    w, s1, e1, s2, e2 = [x for x in re.findall(r"(.+): (\d+)-(\d+) or (\d+)-(\d+)", r)[0]]
    rule[w] = [set(range(int(s1),int(e1)+1)).union(set(range(int(s2),int(e2)+1))), []]

ticks = [ticket.split(",") for ticket in other.split("\n")[1:]]
mytick = [x.split(",") for x in tick.split("\n")[1:]]
valid = [tick for tick in ticks if not any(int(x) not in legal for x in tick)] + mytick
lentick = len(valid[0])
for r, v in rule.items():
    for i in range(lentick):
        if all(int(t[i]) in v[0] for t in valid):
            v[1].append(i)

#this is incredibly ugly
candidates = [(v[1], r) for r, v in rule.items()]
cleaned = []
for i in range(1, lentick+1):
    vals, name = next(filter(lambda x: len(x[0]) == 1 and x[1] not in cleaned, candidates), None)
    val = vals[0]
    for cVals, _ in [c for c in candidates if c[1] != name and c[1] not in cleaned]:
        cVals.remove(val)
    cleaned.append(name)

res = 1
for n in [c[0][0] for c in candidates if "departure" in c[1]]:
    res *= int(mytick[0][n])

print(res)













#part1
#print(sum(int(x) for tick in ticks for x in tick if int(x) not in legal))
#other = [int(x) for o in other.split("\n")[1:] for x in o.split(",")]
#print(sum(o for o in other if o not in legal))
