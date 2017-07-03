#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

import argparse


def pruge(path):
    with open(path) as f:
        result = [l.strip('\n').replace(' ', '').strip('|') for l in f.readlines()]
    return result


def save(data, path):
    with open(path, 'w') as f:
        f.write('\n'.join(data))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('-w', action='store_true')
   
    args = parser.parse_args()

    data = pruge(args.input)
    if args.w:
        save(data, args.input)
    else:
        for i in data:
            print(i)
