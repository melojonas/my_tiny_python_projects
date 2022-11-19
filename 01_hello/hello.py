#!/usr/bin/env python3
'''Autor: Jonas Melo
Purpose: say hello world'''

import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Say hello') 
    parser.add_argument('-n', '--name', metavar='name', default='World', help='Name to greet')
    return parser.parse_args()

def main():
    print(f'Hello, {get_args().name}!')

if __name__ == '__main__': 
    main()
