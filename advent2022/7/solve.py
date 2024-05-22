#!/usr/bin/env python3
import collections.abc
import dataclasses

@dataclasses.dataclass
class File:
    size: int

class Directory(collections.abc.Mapping):
    def __init__(self, parent):
        self._contents = {}
        self.parent = parent
        self.size = 0

    def add_file(self, name, size):
        self._contents[name] = File(size)
        
        directory = self
        while directory is not None:
            directory.size += size
            directory = directory.parent

    def add_dir(self, name):
        self._contents[name] = Directory(parent=self)

    def __getitem__(self, key):
        return self._contents[key]

    def __iter__(self):
        return iter(self._contents)

    def __len__(self):
        return len(self._contents)

def build_filesystem(problem_input):
    cwd = root = Directory(parent=None)
    for line in problem_input.splitlines():
        if line.startswith('$ cd '):
            arg = line[len('$ cd '):]
            if arg == '/':
                cwd = root
            elif arg == '..':
                cwd = cwd.parent
            else:
                cwd = cwd[arg]
        elif not line.startswith('$'):
            size_or_type, name = line.split()
            if name not in cwd:
                if size_or_type == 'dir':
                    cwd.add_dir(name)
                else:
                    cwd.add_file(name, int(size_or_type))
        else:
            assert line == '$ ls', 'Unexpected line'
    return root

def all_directories(filesystem):
    for item in filesystem.values():
        if isinstance(item, Directory):
            yield from all_directories(item)
    yield filesystem

def part1(filesystem):
    total = 0
    for d in all_directories(filesystem):
        if d.size <= 100000:
            total += d.size
    return total

def part2(filesystem):
    available_space = 70000000 - filesystem.size
    needed_space = 30000000 - available_space
    victim = float('inf')
    for d in all_directories(filesystem):
        if d.size >= needed_space:
            victim = min(victim, d.size)
    return victim

def main():
    with open('input') as f:
        filesystem = build_filesystem(f.read())
    print('Part 1:', part1(filesystem))
    print('Part 2:', part2(filesystem))

if __name__ == '__main__':
    main() 
