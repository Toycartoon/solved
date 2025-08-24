import sys

input = sys.stdin.readline

k = int(input())
if k == 1:
    print(0, flush=True)
    print(1, flush=True)
else:
    print(1, flush=True)
    print(1, flush=True)

    ans = int(input())
    print(ans if ans != 0 else k, flush=True)
