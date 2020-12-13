from functools import reduce
import math

lines = [line.strip() for line in open("13.in").readlines()]
est = int(lines[0])
buses = [int(b) for b in lines[1].split(",") if b != "x"]

#part 1
minWait = min([(math.ceil(est/b)*b-est, b) for b in buses])
print(minWait[0] * minWait[1])

#part 2
# I actually solved this with wolfram alpha. typed in (t mod 29) = ((t+19) mod 41) .... = 0 and got the answer
# Later found out about the chinese remainder theorem, this solution below is written by @hermansc
# added it for my own learning

#b = [(int(bus), i) for i, bus in enumerate("17,x,13,19".split(",")) if bus != "x"]
b = [(int(bus), i) for i, bus in enumerate(lines[1].split(",")) if bus != "x"]
i = b[0][0]
t = 0
for bus, offset in b[1:]:
    while (t + offset) % bus != 0:
        t += i
    i *= bus
print(t)
