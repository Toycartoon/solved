import sys

input = sys.stdin.readline

a = [100, 90, 95, 90, 85]
for t in range(int(input())):
    series, know, read, listen = map(int, input().split())
    if (series == 1 or series == 2) and (listen >= 50) and (
            (know * 3 < a[series-1] and read * 3 < a[series-1]) or (series < 4 and (know <= 21 or read <= 21))
    or (series >= 4 and (know + read < 41))):
        print("YES")
    else:
        print("NO")
