b, w = map(int, input().split())
n = 1
while True:
    mn, mx = n ** 2 // 2, n ** 2 // 2
    if n % 2 == 1:
        mx += 1
    
    if min(b, w) >= mn and max(b, w) >= mx:
        n += 1
    else:
        break
print(n-1 if n-1 > 0 else "Impossible")
