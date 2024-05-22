import string

def part1():
    ans = 0
    with open('input') as f:
        for line in f:
            line = line.strip()
            assert len(line) % 2 == 0
            midpoint = len(line) // 2
            compartment1, compartment2 = set(line[:midpoint]), set(line[midpoint:])
            for item in compartment1.intersection(compartment2):
                if item in string.ascii_lowercase:
                    ans += ord(item) - ord('a') + 1
                else:
                    ans += ord(item) - ord('A') + 27
    print(ans)

def part2():
    ans = 0
    with open('input') as f:
        lines = [line.strip() for line in f.readlines()]
    for i in range(0, len(lines), 3):
        s = set(lines[i])
        for j in range(1, 3):
            s = s.intersection(lines[i + j])
        for item in s:
            if item in string.ascii_lowercase:
                ans += ord(item) - ord('a') + 1
            else:
                ans += ord(item) - ord('A') + 27
    print(ans)
