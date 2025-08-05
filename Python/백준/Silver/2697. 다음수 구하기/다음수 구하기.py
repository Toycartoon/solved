import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = input().strip()

    if sorted([*n], reverse=True) == [*n]:
        print("BIGGEST")
        continue

    a = [int(n[-1])]
    for i in range(len(n)-2, -1, -1):
        if int(n[i]) < int(n[i+1]):
            x = min(filter(lambda v: int(v) > int(n[i]), a))
            a.remove(x)
            a.append(int(n[i]))

            print(n[:i], x, *sorted(a), sep="")
            break
        else:
            a.append(int(n[i]))
