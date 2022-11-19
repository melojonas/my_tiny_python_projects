#!/usr/bin/env python3
"""
Author : jonasmelo <jonasmelo@ufrj.br>
Date   : 2022-11-03
Purpose: Picnic game
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    parser.add_argument('-o',
                        '--oxford',
                        help='Insert Oxford comma',
                        action='store_false')
    
    parser.add_argument('-p',
                        '--punctuation',
                        help='Quoted charactor to separate items',
                        default=',')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.item 
    sep = args.punctuation

    num = len(items)

    if args.sorted:
        items.sort()

    if num == 1:
        picnic_list = items[0]
    elif num == 2:
        picnic_list = f'{items[-2]} and {items[-1]}'
    else:
        items[-1] = f'and {items[-1]}'
        if args.oxford:
            picnic_list = str.join(sep+' ', items)
        else:
            picnic_list = f'{sep} '.join(items[:-1]) + f' {items[-1]}'

    print(f'You are bringing {picnic_list}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
