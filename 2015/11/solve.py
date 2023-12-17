#!/usr/bin/env python3

INVALID_CHARS = 'iol'

def has_invalid_chars(password):
    for c in 'iol':
        if c in password:
            return True
    return False

def step_increment(password):
    for i in range(len(password) - 1, -1, -1):
        c = password[i]
        if c != 'z':
            return password[:i] + chr(ord(c) + 1) + password[i+1:]
        else:
            password = password[:i] + 'a' + password[i+1:]
    return 'a' + password

def increment_past_invalid(password):
    assert any(c in password for c in INVALID_CHARS)
    invalid_indicies = [password.find(c) for c in 'iol']
    i = min(i for i in invalid_indicies if i != -1)
    return password[:i] + chr(ord(password[i]) + 1) + 'a' * len(password[i+1:])

def increment_password(password):
    if has_invalid_chars(password):
        return increment_past_invalid(password)
    else:
        return step_increment(password)

def has_increasing_sequence(password):
    for i, j, k in zip(password, password[1:], password[2:]):
        if chr(ord(i) + 1) == j and chr(ord(j) + 1) == k:
            return True
    return False

def has_two_pairs(password):
    # idk if aaaa counts or only aabb. currently this code counts aaaa
    last_char = None
    pair_count = 0
    for c in password:
        if c == last_char:
            pair_count += 1
            if pair_count == 2:
                return True
            last_char = None
        else:
            last_char = c
    return False

def valid_password(password):
    return (has_increasing_sequence(password) and
            not has_invalid_chars(password) and
            has_two_pairs(password))

def part1(puzzle_input):
    password = increment_password(puzzle_input)
    while not valid_password(password):
        password = increment_password(password)
    return password

def part2(puzzle_input):
    return part1(part1(puzzle_input))

def main():
    for puzzle_input in ('hepxcrrq',):
        print(f"Answers for '{puzzle_input}':")
        print('Part 1:', part1(puzzle_input))
        print('Part 2:', part2(puzzle_input))

if __name__ == '__main__':
    main()
