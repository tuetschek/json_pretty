#!/usr/bin/env python3

import json
import random
from argparse import ArgumentParser
import sys

random.seed(1206)


if __name__ == '__main__':

    ap = ArgumentParser(description='Pretty print JSON files + select just random examples')
    ap.add_argument('--select', '-s', type=int, help='Select N random examples')
    ap.add_argument('input_file', nargs='?', type=str, default='-', help='Input file (defaults to stdin)')
    args = ap.parse_args()

    if args.input_file != '-':
        fh = open(args.input_file, 'r', encoding='UTF-8')
    else:
        fh = sys.stdin

    data = json.load(fh)

    if args.select and isinstance(data, list):
        data = random.sample(data, args.select)

    print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))
