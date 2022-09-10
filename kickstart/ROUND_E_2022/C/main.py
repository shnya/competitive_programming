import sys
import copy
from bisect import bisect_right

MOD = (1 << 61) - 1
BASE = 10007

class RollingHash():

    def __init__(self, s, base = BASE, mod = MOD):
        self.mod = mod
        self.pw = pw = [1]*(len(s)+1)

        l = len(s)
        self.h = h = [0]*(l+1)

        v = 0
        for i in range(l):
            h[i+1] = v = (v * base + ord(s[i])) % mod
        v = 1
        for i in range(l):
            pw[i+1] = v = v * base % mod

    def get(self, l, r):
        return (self.h[r] - self.h[l] * self.pw[r-l]) % self.mod


def is_palindrome(s, l, r, rhash, rev_rhash):
    leng = r - l
    if leng == 1:
        return True
    #print(s[l:r])
    if leng % 2 == 0:
        right = leng // 2
        left = leng // 2 - 1
        #print(l, l+left+1, l + right, r, s[l:l+left+1], rev_rhash.get(l, l + left + 1), s[l + right:r], rhash.get(l + right, r))
        return rhash.get(l + right, r) == rev_rhash.get(len(s) - (l + left + 1), len(s) - l)
    else:
        right = leng // 2 + 1
        left = leng // 2 - 1
        #print(l, l+left+1, l + right, r, s[l:l+left+1], rev_rhash.get(l, l + left + 1), s[l + right:r], rhash.get(l + right, r))
        return rhash.get(l + right, r) == rev_rhash.get(len(s) - (l + left + 1), len(s) - l)

def solve(s):
    N = len(s)
    rhash = RollingHash(s)
    rev_rhash = RollingHash("".join(reversed(list(s))))
    for i in range(1, N):
        if is_palindrome(s, 0, i, rhash, rev_rhash) and is_palindrome(s, i, N, rhash, rev_rhash):
            return s[0:i]
    return s


N = int(sys.stdin.readline())
for i in range(N):
    k = int(sys.stdin.readline())
    l = sys.stdin.readline().rstrip()
    print(f"Case #{i+1}: {solve(l)}")