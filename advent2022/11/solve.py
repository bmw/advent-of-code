#!/usr/bin/env python3
import copy
import dataclasses
import functools
import operator
import typing

@dataclasses.dataclass
class Monkey:
    items: typing.List[int]
    operation: str
    divisor: int
    true_target: int
    false_target: int
    inspection_count: int = 0

    def new_worry_level(self, old):
        return eval(self.operation)

    def inspect_all(self):
        for i, item in enumerate(self.items):
            self.items[i] = self.new_worry_level(item)
            self.inspection_count += 1

    def throw_all(self):
        result = []
        for item in self.items:
            target = self.true_target if item % self.divisor == 0 else self.false_target
            result.append((item, target))
        self.items.clear()
        return result

    @classmethod
    def from_input(cls, lines):
        assert lines[0].startswith('Monkey')
        items = [int(s) for s in lines[1].partition(':')[2].split(',')]
        operation = lines[2].partition('=')[2]
        divisor = int(lines[3].split()[-1])
        true_target = int(lines[4].split()[-1])
        false_target = int(lines[5].split()[-1])
        target = lambda worry: true_target if worry % divisor == 0 else false_target
        return cls(items, operation, divisor, true_target, false_target)

def simulate_throws(all_monkeys, throwing_monkey):
    for item, target in throwing_monkey.throw_all():
        all_monkeys[target].items.append(item)

def part1(monkeys):
    for _ in range(20):
        for monkey in monkeys:
            monkey.inspect_all()
            monkey.items = [item // 3 for item in monkey.items]
            simulate_throws(monkeys, monkey)
    return functools.reduce(operator.mul, sorted(monkey.inspection_count for monkey in monkeys)[-2:])

def part2(monkeys):
    divisor_product = functools.reduce(operator.mul, (monkey.divisor for monkey in monkeys))
    for _ in range(10000):
        for monkey in monkeys:
            monkey.inspect_all()
            monkey.items = [item % divisor_product for item in monkey.items]
            simulate_throws(monkeys, monkey)
    return functools.reduce(operator.mul, sorted(monkey.inspection_count for monkey in monkeys)[-2:])

def main():
    for filename in ('example', 'input'):
        with open(filename) as f:
            monkey_inputs = f.read().split('\n\n')
        monkeys = [Monkey.from_input(monkey_input.splitlines()) for monkey_input in monkey_inputs]
        print(f"Answers for '{filename}':")
        print('Part 1:', part1(copy.deepcopy(monkeys)))
        print('Part 2:', part2(monkeys))

if __name__ == '__main__':
    main()
