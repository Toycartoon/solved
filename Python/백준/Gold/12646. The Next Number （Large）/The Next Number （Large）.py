import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = input().strip()

    if sorted([*n], reverse=True) == [*n]:
        print(f"Case #{t+1}: ", end="")
        a = list(sorted([*n]))
        z = 0
        idx = -1
        for i in range(len(a)):
            if a[i] != "0":
                idx = i
                break
            z += 1
        print(a[idx], 0, "0" * z, *a[idx+1:], sep="")
        continue

    a = [int(n[-1])]
    for i in range(len(n)-2, -1, -1):
        if int(n[i]) < int(n[i+1]):
            x = min(filter(lambda v: int(v) > int(n[i]), a))
            a.remove(x)
            a.append(int(n[i]))

            print(f"Case #{t+1}: ", end="")
            print(n[:i], x, *sorted(a), sep="")
            break
        else:
            a.append(int(n[i]))
