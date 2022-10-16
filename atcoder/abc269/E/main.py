#!/usr/bin/env python3
import sys


def send(A, B, C, D):
    print(f"? {A} {B} {C} {D}", flush=True)
    return int(sys.stdin.readline())
   

def main():
    N = int(sys.stdin.readline())
    U = 1
    D = N + 1
    while U + 1 != D:
        M = (U + D) // 2
        c = send(U, M - 1, 1, N)
        if c == M - U:
            U = M
        else:
            D = M
    
    L = 1
    R = N + 1
    while L + 1 != R:
        M = (L + R) // 2
        c = send(1, N, L, M - 1)
        if c == M - L:
            L = M
        else:
            R = M
    print(f"! {U} {L}", flush=True)
    

if __name__ == '__main__':
    main()
