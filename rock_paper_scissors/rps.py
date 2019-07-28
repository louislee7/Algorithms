#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    result = []
    plays = ['rock', 'paper', 'scissors']

    def helper(action, rounds):
        if rounds == 0:
            return result.append(action)
        else:
            for play in plays:
                helper([*action, play], rounds - 1)

    helper([], n)
    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
