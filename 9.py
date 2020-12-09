from itertools import combinations

lines = [int(line.strip()) for line in open("9.in").readlines()]

preamblelen = 25
res = 0
i = 0
while True:
    combs = combinations(lines[i:i+preamblelen+1], 2)
    if any(a+b == lines[i+preamblelen+1] for a,b in combs):
        i+=1
        continue
    res = lines[i+preamblelen+1]
    break

#part 1
print(res)

#part 2
j = 0
indexes = []
res2 = 0
while True:
    res2 += lines[j]
    indexes.append((j, lines[j]))
    if res2 == res:
        print(max(l[1] for l in indexes) + min(l[1] for l in indexes))
        break;
    if res2 > res:
        j = indexes[0][0]
        indexes = []
        res2 = 0
    j += 1
