#!/usr/bin/env python3

OPENERS = '([{<'
CLOSERS = ')]}>'
CLOSERS2OPENERS = {c: o for c, o in zip(CLOSERS, OPENERS)}
OPENERS2CLOSERS = {v: k for k, v in CLOSERS2OPENERS.items()}
ILLEGAL_CHAR_SCORE = {c: v for c, v in zip(CLOSERS, (3, 57, 1197, 25137,))}
COMPLETION_SCORE = {c: v for c, v in zip(CLOSERS, range(1, 5))}

def get_input():
    with open('10.txt') as f:
        return f.read().splitlines()

def corruption_score(line):
    opener_stack = []
    for c in line:
        if c in OPENERS:
            opener_stack.append(c)
        elif c in CLOSERS:
            if opener_stack and opener_stack[-1] == CLOSERS2OPENERS[c]:
                opener_stack.pop()
            else:
                return ILLEGAL_CHAR_SCORE[c]
        else:
            raise ValueError
    return 0

def is_corrupted(line):
    opener_stack = []
    for c in line:
        if c in OPENERS:
            opener_stack.append(c)
        elif c in CLOSERS:
            if opener_stack and opener_stack[-1] == CLOSERS2OPENERS[c]:
                opener_stack.pop()
            else:
                return True
        else:
            raise ValueError
    return False

def get_completion_string(line):
    opener_stack = []
    for c in line:
        if c in OPENERS:
            opener_stack.append(c)
        elif c in CLOSERS:
            opener_stack.pop()
    return ''.join(OPENERS2CLOSERS[o] for o in opener_stack[::-1])

def get_completion_score(line):
    completion = get_completion_string(line)
    score = 0
    for c in completion:
        score *= 5
        score += COMPLETION_SCORE[c]
    return score

def main1():
    print(sum(corruption_score(l) for l in get_input()))

def main2():
    uncorrupted = [l for l in get_input() if not is_corrupted(l)]
    scores = sorted(get_completion_score(l) for l in uncorrupted)
    print(scores[len(scores)//2])

if __name__ == '__main__':
    main2()
