#!/usr/bin/env python3
import sys

MOD = 4  # type: int


def calc_score(N, p, move):
    score = 0
    #print(N, p, move)
    for i in range(N):
        new_p = p[i] + move
        if new_p < 0:
            new_p = N + new_p
        elif new_p > N:
            new_p = new_p % N
        #print(i, new_p)
        if i < new_p:
            score += min(new_p - i, i + N - new_p)
        else:
            score += min(i - new_p, new_p + N - i)
    return score


def find_proper(p, N, dists, dir):
    sums = {}
    for i in range(N):
        sums[dists[i]] = sums.get(dists[i], 0) + 1
    mean = sum(dists) // len(dists)
    min_n = calc_score(N, p, mean * dir)
    min_n = min(min_n, calc_score(N, p, (mean - 1) * dir))
    min_n = min(min_n, calc_score(N, p, (mean + 1) * dir))
    return min_n


def solve(N: int, p: "List[int]"):
    idx = {}
    for i in range(len(p)):
        idx[p[i]] = i
    
    # 左回り
    dists = [0] * N
    for i in range(N):
        if p[i] > i:
            dist = N - (p[i] - i)
        else:
            dist = i - p[i]
        dists[i] = dist
    min_n = find_proper(p, N, dists, -1)

    # 右回り
    dists = [0] * N
    for i in range(N):
        if p[i] < i:
            dist = N - (i - p[i])
        else:
            dist = p[i] - i
        dists[i] = dist
    min_n = min(min_n, find_proper(p, N, dists, 1))
    print(min_n)

    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, p)

if __name__ == '__main__':
    main()
