while True:
    n = int(input())
    if n == 0:
        break

    l, r = 0, 51
    a = []
    while l < r:
        mid = (l + r) // 2
        a.append(mid)
        
        if mid == n:
            break
        elif mid < n:
            l = mid
        else:
            r = mid
    
    print(*a)
