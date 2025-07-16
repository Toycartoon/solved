n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

for i in sorted(list(a & b)):
    print(i)
