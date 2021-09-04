#!/usr/bin/env python3
from copy import deepcopy


def map_neighbours(R, C, G):
    G = deepcopy(G)
    corners = []

    for r in range(R):
        for c in range(C):
            # init [up, down, left, right]
            G[r][c] = [G[r][c]] * 4
            if r > 0 and G[r][c][0]:  # up
                G[r][c][0] += G[r - 1][c][0]
            if c > 0 and G[r][c][2]:  # left
                G[r][c][2] += G[r][c - 1][2]

    for r in range(R - 1, -1, -1):
        for c in range(C - 1, -1, -1):
            if r < (R - 1) and G[r][c][1]:  # down
                G[r][c][1] += G[r + 1][c][1]
            if c < (C - 1) and G[r][c][3]:  # right
                G[r][c][3] += G[r][c + 1][3]

            if G[r][c][0] + G[r][c][1] - 2 > 0 and G[r][c][2] + G[r][c][3] - 2 > 0:
                corners.append((r, c))
    return G, corners


def check_corner(G, r, c):
    # [up, down, left, right]
    up, down, left, right = G[r][c]

    L = 0
    for updown in G[r][c][:2]:
        for leftright in G[r][c][2:]:
            if updown >= 2 and leftright >= 4:
                L += min(updown, leftright // 2) - 1
            if leftright >= 2 and updown >= 4:
                L += min(updown // 2, leftright) - 1
    return L


def ans(R, C, G):
    """
    The segments must share one cell that is an endpoint of both segments.
    * Segments must have length at least 2.
    * The length of the longer segment is twice the length of the shorter segment.
    """
    NG, corners = map_neighbours(R, C, G)

    return sum(check_corner(NG, *corner) for corner in corners)


for t in range(int(input())):
    R, C = input().split(" ")
    G = [list(map(int, input().split(" "))) for _ in range(int(R))]

    print(f"Case #{t+1}: {ans(int(R), int(C), G)}")
