#!/usr/bin/env python3
import sys

sys.setrecursionlimit(1000000)

MAXL = 2**63-1


def solve(N: int, M: int, K: int, A: "List[int]", B: "List[int]", C: "List[int]", E: "List[int]"):
    dp = [MAXL for x in range(N + 1)]
    dp[1] = 0
    for i in range(K):
        cur_city = A[E[i] - 1]
        target = B[E[i] - 1]
        score = C[E[i] - 1]
        if dp[cur_city] == MAXL:
            continue
        dp[target] = min(dp[cur_city] + score, dp[target])
    if dp[N] == MAXL:
        print(-1)
    else:
        print(dp[N])
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    C = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    E = [int(next(tokens)) for _ in range(K)]  # type: "List[int]"
    solve(N, M, K, A, B, C, E)

if __name__ == '__main__':
    main()
