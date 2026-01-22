import sys

input = sys.stdin.readline    # 크아악 FastIO를 요구하다니

for t in range(int(input())):
    k, c, p = map(int, input().split())
    if k + c + p == 1 or (k == 1 and (c == 0 and p < 2)) or (k > 1 and c + p < 2):
        print("N")
    else:
        print("Y")
