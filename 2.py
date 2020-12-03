import re

valid1 = 0
valid2 = 0

pattern = re.compile(r'(\d+)-(\d+) (\w): (\w*)')

def parse(line):
    lo, hi, char, string = re.match(pattern, line).groups()
    return int(lo), int(hi), char, string

for line in open("2.in").readlines():
    lo, hi, char, password = parse(line)
    if lo <= password.count(char) <= hi:
        valid1 += 1
    if sum([1 if password[bound-1] == char else 0 for bound in [lo, hi]]) == 1 :
        valid2 += 1

print(valid1)
print(valid2)
