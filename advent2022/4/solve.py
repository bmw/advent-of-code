def part1():
    ans = 0
    with open('input') as f:
        for line in f:
            low1, high1, low2, high2 = (int(v) for s in line.strip().split(',') for v in s.split('-'))
            if (low1 <= low2 and high2 <= high1) or (low2 <= low1 and high1 <= high2):
                ans += 1
    print(ans)

def part2():
    ans = 0
    with open('input') as f:
        for line in f:
            low1, high1, low2, high2 = (int(v) for s in line.strip().split(',') for v in s.split('-'))
            if low1 <= low2 <= high1 or low2 <= low1 <= high2:
                ans += 1
    print(ans)

part2()
