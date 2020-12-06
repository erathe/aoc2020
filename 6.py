from collections import Counter

lines = [line.strip() for line in open("6.in").read().split("\n\n")]

#part 1
print(sum([len(set(line.replace("\n", ""))) for line in lines]))

#part 2
print(len([c for block in lines for c, i in Counter(block).items() if i == len(block.split("\n"))]))
