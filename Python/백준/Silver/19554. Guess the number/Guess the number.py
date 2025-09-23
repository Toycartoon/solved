n = int(input())
l, r = 0, n+1
while l < r:
    mid = (l + r) // 2
    print(f"? {mid}")

    p = int(input())
    if p == 0:
        print(f"= {mid}")
        break
    elif p == -1:
        l = mid
    else:
        r = mid
