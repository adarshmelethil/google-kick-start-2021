#!/usr/bin/env python3


def good_score(S, N):
    score = 0
    for i, ab in enumerate(zip(S, S[::-1])):
        a, b = ab
        if i == N // 2:
            break
        if a != b:
            score += 1
    return score


def ans(N, K, S):

    return abs(K - good_score(S, N))


for t in range(int(input())):
    N, K = input().split(" ")
    S = input()
    print(f"Case #{t+1}: {ans(int(N), int(K), S)}")
