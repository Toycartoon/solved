n = int(input())
a = list(map(int, input().split()))
x = int(input())

a.sort()
l, r = 0, n-1

ans  = 0
while l < r:
    m = a[l] + a[r]

    if m < x:
        l += 1
    elif m > x:
        r -= 1
    else:
        ans += 1
        l += 1

print(ans)
