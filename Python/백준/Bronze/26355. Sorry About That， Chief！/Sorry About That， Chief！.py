a = [i for i in range(10008)]
a[1] = 0
for i in range(2, int(len(a) ** 0.5)+1):
    if a[i] == 0:
        continue

    for j in range(i * i, len(a), i):
        a[j] = 0

s = []
for i in a:
    if i != 0:
        s.append(i)

for t in range(int(input())):
    n = int(input())
    print(f"Input value: {n}")

    if n in s:
        print("Would you believe it; it is a prime!")
    else:
        idx = 0
        while s[idx] < n:
            idx += 1
        print(f"Missed it by that much ({min(abs(s[idx-1]-n), abs(s[idx]-n))})!")
    print()
