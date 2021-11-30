import re
lines = [line.strip() for line in open("18.in").readlines()]

class Num:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Num(self.num * other.num)

    def __sub__(self, other):
        return Num(self.num + other.num)

    def __mul__(self, other):
        return Num(self.num + other.num)

tr = str.maketrans("+*", "-+")

def solve(line):
    ev = str.translate(line, tr)
    return re.sub(r'(\d+)', r'Num(\1)', tr)

pr = [solve(line) for line in lines]
print(pr)
res = map(lambda l: eval(l).num, pr)
print(sum(res))
