n = int(input())
a = list(map(int, input().split()))

f = True
decrease = False
for i in range(1, n):
    if a[i-1] == a[i]:
        f = False
        break
    elif a[i-1] > a[i]:
        if not decrease:
            decrease = True
    else:
        if decrease:
            f = False
            break
print("YES" if f else "NO")
