inst = [line.strip() for line in open("8.in").readlines()]

instructions = {
        "jmp": (lambda i, acc, arg: (i + int(arg), acc)),
        "acc": (lambda i, acc, arg: (i + 1, acc + int(arg))),
        "nop": (lambda i, acc, arg: (i + 1, acc))
        }

def run_boot(commands):
    visited = set()
    finished = False
    acc = j = 0
    while not j in visited:
        if j > len(commands) - 1:
            finished = True
            break
        visited.add(j)
        comm, arg = commands[j].split()
        j, acc = instructions[comm](j, acc, arg)
    return (finished, acc)

#part 1
print(run_boot(inst)[1])

#part 2
complete_instructions = []
for i, line in enumerate(inst):
    if line[0:3] == "jmp":
        copy = inst.copy()
        copy[i] = "nop" + line[3:]
        complete_instructions.append(copy)
        continue
    if line[0:3] == "nop":
        copy = inst.copy()
        copy[i] = "jmp" + line[3:]
        complete_instructions.append(copy)
        continue

for line in complete_instructions:
    success, accumulator = run_boot(line)
    if success:
        print(accumulator)
        break
