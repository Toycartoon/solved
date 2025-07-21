import sys

input = sys.stdin.readline

for k in range(int(input())):
    n, w, e = map(int, input().split())
    ans = 0
    for i in range(n):
        lww, lwe, lew, lee = map(int, input().split())
        ans += max(lww * w + lew * e, lwe * w + lee * e)

    print(f"Data Set {k+1}:")
    print(ans)
    print()
