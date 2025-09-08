l = int(input())
r = int(input())

ans = 0
for i in range(l, r+1):
    v = 0
    for x in range(1, i+1):
        if i % x == 0:
            v += 1

    if v == 4:
        ans += 1

print(f"The number of RSA numbers between {l} and {r} is {ans}")
