#!/usr/bin/env python3
import sys

WEEKS = {
    "Monday": 5, 
    "Tuesday": 4, 
    "Wednesday": 3, 
    "Thursday": 2, 
    "Friday": 1
}


def solve(S: str):
    print(WEEKS[S])


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)

if __name__ == '__main__':
    main()