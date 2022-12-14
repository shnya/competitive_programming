#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(S: str):
    if S[0] == "1":
        print(NO)
        return
    line = [0] * 7
    for i in range(1, 10):
        if i >= 6 and S[i] == "1":
#            print(i, (i-6) * 2)
            line[(i - 6) * 2] += 1
        elif i >= 3 and S[i] == "1":
#            print(i, (i-3) * 2 + 1)
            line[(i - 3) * 2 + 1] += 1
        elif S[i] == "1":
#            print(i, i*2)
            line[i * 2] += 1
    has_pin = False
    has_split = False
    #print(line)
    for i in range(7):
        if has_pin:
            if line[i] == 0:
                has_split = True
                continue
            elif has_split:
                print(YES)
                return
            else:
                continue
        else:
            if line[i] > 0:
                has_pin = True
                has_split = False
            else:
                continue

    print(NO)


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
