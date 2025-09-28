a = list(map(int, input().split()))
if a.count(0) == 1:
    print(a.index(0)+1, 10-sum(a))
elif a.count(0) == 2:
    print(*sorted({*range(1, 5)}-{*a}))
else:
    print(*a[:2])
