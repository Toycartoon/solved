a = list(map(int, input().split()))
mx = max(a)
if a[-1] == mx and a.count(mx) == 1:
    print(mx)
else:
    print(mx+1)
