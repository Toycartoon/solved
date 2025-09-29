import sys

input = sys.stdin.readline

for t in range(int(input())):
    a = []
    for i in range(int(input())):
        s = input().strip()
        a.append((len({*s.replace(" ", "")}), s))
    a.sort(key=lambda x: (-x[0], x[1]))
    print(f"Case #{t+1}: {a[0][1]}")
