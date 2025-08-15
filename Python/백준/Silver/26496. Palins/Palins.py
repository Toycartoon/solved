import sys

input = sys.stdin.readline

while True:
    s = input().strip()
    if len(s) == 0:
        break

    ans = set()
    for i in range(1, len(s)+1):
        for j in range(i, len(s) + 1):
            v = s[j-i:j]
            if v == v[::-1]:
                ans.add(v)

    print(f"{len(ans)} - ", end="")
    for i in sorted(list(ans), key=lambda x: (len(x), s.index(x))):
        print(f"\"{i}\"", end=" ")
    print()
