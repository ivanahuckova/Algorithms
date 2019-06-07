#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    results = []
    options = ["rock", "paper", "scissors"]

    def play(played, n):
        if n == 0:
            return results.append(played)
        else:
            for i in range(3):
                play(played + [options[i]], n-1)
    play([], n)
    return results


print(rock_paper_scissors(3))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
