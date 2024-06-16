#!/usr/bin/env python3
import collections

CHARSET = 'abcdefg'
SIGNAL2DISPLAY = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
}

Entry = collections.namedtuple('Entry', 'signals outputs')

def read_entries():
    entries = []
    with open('8.txt') as f:
        for line in f:
            signals, _, outputs = line.strip().partition(' | ')
            entries.append(Entry(signals.split(), outputs.split()))
    return entries

# part 1
# def main():
#     answer = 0
#     for entry in read_entries():
#         for output in entry.outputs:
#             if len(output) in (2, 3, 4, 7):
#                 answer += 1
#     print(answer)

def missing_signals(pattern):
    missing = ''.join(c for c in CHARSET if c not in pattern)
    return missing

def filter_out(mapping, signal, exclusions):
    for c in exclusions:
        mapping[signal] = mapping[signal].replace(c, '')

def filter_to(mapping, signal, possibilities):
    mapping[signal] = ''.join(c for c in mapping[signal] if c in possibilities)

def filter_taken(possible_mapping):
    taken_signals = []
    for mapping in possible_mapping.values():
        if len(mapping) == 1:
            taken_signals.append(mapping)
    for c in CHARSET:
        if len(possible_mapping[c]) != 1:
            for c2 in taken_signals:
                possible_mapping[c] = possible_mapping[c].replace(c2, '')

def frequency_analysis(signals):
    possible_mapping = {c: CHARSET for c in CHARSET}
    for signal in signals:
        if len(signal) == 2:
            for c in CHARSET:
                if c in signal:
                    filter_to(possible_mapping, c, 'cf')
                else:
                    filter_out(possible_mapping, c, 'cf')
        elif len(signal) == 3:
            for c in CHARSET:
                if c in signal:
                    filter_to(possible_mapping, c, 'acf')
                else:
                    filter_out(possible_mapping, c, 'acf')
        elif len(signal) == 4:
            for c in CHARSET:
                if c in signal:
                    filter_to(possible_mapping, c, 'bcdf')
                else:
                    filter_out(possible_mapping, c, 'bcdf')
        elif len(signal) == 5:
            missing = missing_signals(signal)
            assert len(missing) == 2
            for c in missing:
                filter_out(possible_mapping, c, 'adg')
        elif len(signal) == 6:
            missing = missing_signals(signal)
            assert len(missing) == 1
            filter_to(possible_mapping, missing, 'cde')
    return possible_mapping

def get_mapping(signals):
    mapping = frequency_analysis(signals)
    filter_taken(mapping)
    assert sum(len(s) for s in mapping.values()) == 7

    # convert for use with str.translate
    return {ord(k): ord(v) for k, v in mapping.items()}

def main():
    total = 0
    for entry in read_entries():
        num = 0
        ord_mapping = get_mapping(entry.signals)
        for output in entry.outputs:
            output = ''.join(sorted(output.translate(ord_mapping)))
            if output not in SIGNAL2DISPLAY:
                assert False, output
            else:
                num *= 10
                num += SIGNAL2DISPLAY[output]
        total += num
    print(total)


if __name__ == '__main__':
    main()
