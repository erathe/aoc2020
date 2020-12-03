lines = [int(line.strip()) for line in open('inp1.in').readlines()]

for line in lines:
    for y in lines[1:]:
        for x in lines[2:]:
            if x + y + line == 2020:
                print(line*y*x)
