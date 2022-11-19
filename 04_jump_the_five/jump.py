#!/usr/bin/env python3
"""
Author : jonasmelo <jonasmelo@ufrj.br>
Date   : 2022-11-03
Purpose: Jump the Five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('phrase',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    phrase = args.phrase
    ph_list = [x for x in phrase]

    jumper = {'1':'9',
                '2':'8',
                '3':'7',
                '4':'6',
                '5':'0',
                '6':'4',
                '7':'3',
                '8':'2',
                '9':'1',
                '0':'5'}

    i = 0
    for x in ph_list:
        if x.isdigit():
            ph_list[i] = jumper[x]
        i += 1

    print(''.join(ph_list))


# --------------------------------------------------
if __name__ == '__main__':
    main()
