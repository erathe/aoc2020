from collections import defaultdict
from itertools import combinations
import re

lines = [line.strip() for line in open("14.in").readlines()]

bitmask = ['0'] * 36
memory = defaultdict(lambda: 0)


#use set(combinations)
for line in lines:
    if "mask" in line:
        bitmask = list(line.split(" = ")[1][::-1])
    else:
        idx = []
        combs = []
        mem, val = [int(x) for x in re.match(r"mem\[(\d+)\] = (\d+)", line).groups()]
        mem = bin(mem)[2:][::-1]
        mMem = []
        masks = []
        for i, c in enumerate(bitmask):
            if c == "X":
                idx.append(i)
                combs.extend(['1', '0'])
                mMem.append(c)
            elif i > len(mem) - 1:
                mMem.append(c)
            else:
                mMem.append(c if c == '1' else mem[i])
        for c in set(combinations(combs, len(idx))):
            nMem = mMem.copy()
            for i in range(len(idx)):
                nMem[idx[i]] = c[i]
            masks.append(nMem)
        for mask in masks:
            memory[int("0b" + "".join(mask)[::-1], 2)] = val

        #memory[mem] = int('0b' + mVal[::-1], 2)

#for line in lines:
#    if "mask" in line:
#        bitmask = list(line.split(" = ")[1][::-1])
#    else:
#        mem, val = [int(x) for x in re.match(r"mem\[(\d+)\] = (\d+)", line).groups()]
#        val = bin(val)[2:][::-1]
#        mVal = ''
#        for i, c in enumerate(bitmask):
#            if i > len(val) - 1:
#                mVal += '1' if c == '1' else '0'
#            elif c in ["X"]:
#                mVal += val[i]
#            else:
#                mVal += c if c == '1' else val[i]
#        memory[mem] = int('0b' + mVal[::-1], 2)

# part 1
print(sum(v for v in memory.values()))
