n = int(input())
a = list(map(int, input().split()))

i = sum(a[:a.index(max(a))])
j = sum(a[a.index(max(a))+1:])

print(i)
print(j)
