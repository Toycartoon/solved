import sys

input = sys.stdin.readline

for t in range(int(input())):
    w = {}
    for i in range(int(input())):
        a, b = input().strip().split()
        w[a] = b

    print(f"Test case #{t+1}:")
    for i in range(int(input())):
        s = input().strip()
        v = ""
        for x in s:
            if x in w:
                v += w[x]
            else:
                v += x

        print(s, "YES" if v == v[::-1] else "NO")
    print()
