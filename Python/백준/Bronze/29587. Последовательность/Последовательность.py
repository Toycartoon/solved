n = int(input())
a = list(map(int, input().split()))

if sorted(a) == a and len({*a}) == n:
    print(0)
else:
    print(n)
    print(*range(1, n+1))
