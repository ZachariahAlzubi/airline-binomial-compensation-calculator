import math
import matplotlib.pyplot as plt

def binomial_prob(N, p, y):
    # calculates the binomial probability
    return math.comb(N, y) * (p ** y) * ((1 - p) ** (N - y))

def plot_binomial_prob(N, p):
    x = []
    y = []
    i = 0
    for y_ in range(N + 1):
        bp = binomial_prob(N, p, y_)
        x.append(i)
        y.append(bp * 100)
        i += 1
    plt.plot(x, y)
    plt.xlabel("Iteration Number")
    plt.ylabel("Binomial Probability (%)")
    plt.title("Binomial Probability vs Iteration Number")
    plt.show()

def expected_value(N, p):
    # calculates the expected value of the number of empty seats
    ev = 0
    for y in range(N + 1):
        ev += y * binomial_prob(N, p, y)
    return ev

def max_compensation(N, p, L, m):
    # calculates the maximum compensation offered to each passenger
    ev = expected_value(N, p)
    R = (ev * L) / m
    return R

def average_compensation(L, m):
    compensation = []
    for N in range(90, 101):
        for oversold in range(1, 11):
            p = N / 100
            result = max_compensation(N + oversold, p, L, m)
            compensation.append(result)
    avg_comp = sum(compensation) / len(compensation)
    return avg_comp
