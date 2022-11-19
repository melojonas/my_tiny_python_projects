#!/usr/bin/env python3
"""
Author : jonasmelo <jonasmelo@ufrj.br>
Date   : 2022-11-02
Purpose: Crow's Nest
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """main"""

    args = get_args()
    word = args.word
    article = 'an' if args.word[0] in 'aeiouAEIOU' else 'a'
    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
