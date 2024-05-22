PART1 = False
             
def build_stacks(f):
    lines = []
    stacks = []
    line = f.readline().rstrip()
    while line:
        lines.append(line)
        line = f.readline().rstrip()
    for i, c in enumerate(lines[-1]):
        if not c.isspace():
            stacks.append([])
            j = len(lines) - 2
            while j >= 0 and i < len(lines[j]) and not lines[j][i].isspace():
                stacks[-1].append(lines[j][i])
                j -= 1
    return stacks

with open('input') as f:
    stacks = build_stacks(f)
    for line in f:
        line = line.strip()
        crate_count, source, dest = (int(s) for s in line.split()[1::2])
        if PART1:
            for _ in range(crate_count):
                stacks[dest - 1].append(stacks[source - 1].pop())
        else:
            stacks[dest - 1].extend(stacks[source - 1][-crate_count:])
            stacks[source - 1] = stacks[source - 1][:-crate_count]
    print(''.join(stack[-1] for stack in stacks))
