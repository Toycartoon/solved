from math import trunc

k1, o1, k2, o2, k3 = input().split()
a = [eval(f"trunc((trunc({k1+o1+k2})){o2+k3})"), eval(f"trunc({k1+o1}trunc(({k2+o2+k3})))")]
a.sort()

print(a[0])
print(a[1])
