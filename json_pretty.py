#!/usr/bin/env python3

import json
import random
from argparse import ArgumentParser
import sys

random.seed(1206)


if __name__ == '__main__':

    ap = ArgumentParser(description='Pretty print JSON files + select just random examples')
    ap.add_argument('--select', '-s', type=int, help='Select N random examples')
    ap.add_argument('--indent', '-i', type=int, help='Indent width', default=4)
    ap.add_argument('--max-depth', '-m', type=int, help='Max depth for indentation', default=0)
    ap.add_argument('input_file', nargs='?', type=str, default='-', help='Input file (defaults to stdin)')
    args = ap.parse_args()

    if args.input_file != '-':
        fh = open(args.input_file, 'r', encoding='UTF-8')
    else:
        fh = sys.stdin

    data = json.load(fh)

    if args.select and isinstance(data, list):
        data = random.sample(data, args.select)

    lines = json.dumps(data, sort_keys=True, indent=args.indent, ensure_ascii=False).split('\n')
    out = []
    if args.max_depth:
        for line in lines:
            if line.startswith((args.max_depth * args.indent) * ' ') or line.startswith(((args.max_depth - 1) * args.indent) * ' ') and line.strip() in ['}', '},', '],', ']']:
                out[-1] = out[-1] + line.lstrip()
            else:
                out.append(line)
    else:
        out = lines

    print('\n'.join(out))
