n = int(input())
d = list(map(int, input().split()))

a = d[0] // 3
c = d[-1] // 3
b = d[1] - a * 2
print(a, b, c)
