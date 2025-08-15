import sys

input = sys.stdin.readline

a = []
for t in range(int(input())):
    l, *v = input().strip().split()
    a.append((l, set(" ".join(v).lower().split())))

_ = input()
while True:
    s = set(input().strip().replace(",", " ").replace(".", " ").replace("!", " ").replace(";", " ").replace("?", " ")
            .replace("(", " ").replace(")", " ").lower().split())
    if len(s) == 0:
        break

    for i in a:
        if len(i[1] & s) != 0:
            print(i[0])
            break
