lines = [(row.strip()[0], int(row.strip()[1:])) for row in open("12.in").readlines()]

rot = {
        90: 1,
        180: 2,
        270: 3
        }

moves = {
        "N": (lambda x,y,s: (x,y+s)),
        "E": (lambda x,y,s: (x+s,y)),
        "S": (lambda x,y,s: (x,y-s)),
        "W": (lambda x,y,s: (x-s,y)),
        }
rotatep = {
        "L": (lambda x,y: (-y, x)),
        "R": (lambda x,y: (y, -x))
        }

x = y = 0
xw = 10
yw = 1
for c, s in lines:
    if c in ["L", "R"]:
        for _ in range(rot[s]):
            (xw, yw) = rotatep[c](xw, yw)
    elif c == "F":
        x, y = (x + (s * xw), y + (s * yw))
    else:
        xw, yw = moves[c](xw, yw, s)

print(abs(x) + abs(y))
