#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

def generate_score_dist():
    win_prob = np.array(
        [0.78, 0.96, 0.84, 0.33, 0.56, 0.51, 0.78, 0.57, 0.78, 0.32, 0.62,
         0.39])
    samples = np.array([win_prob > np.random.rand(12) for _ in xrange(1000000)],
                       dtype=int)
    wins = samples.sum(axis=1)
    counts = np.array(
        [(wins == x*np.ones(wins.size)).sum() for x in xrange(13)])
    return counts/float(sum(counts))

def main():
    width = 0.6
    ind = np.arange(13)

    plt.bar(ind, generate_score_dist(), width=width)
    plt.xticks(ind + width/2., [str(x) for x in xrange(13)])
    plt.xlabel("Wins")

    plt.savefig("wins.png")

if __name__ == "__main__":
    main()
