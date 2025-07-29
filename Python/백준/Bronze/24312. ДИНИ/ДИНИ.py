a = list(map(int, input().split()))
a.sort()
print(min(abs(a[3]-sum(a[:3])), abs(a[0]+a[3]-a[2]-a[1])))
