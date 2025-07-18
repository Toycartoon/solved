from math import sqrt

for t in range(int(input())):
    a, b, c = map(float, input().split())
    mx = (-b + sqrt(b ** 2 - (4 * a * c))) / (2 * a)
    mn = (-b - sqrt(b ** 2 - (4 * a * c))) / (2 * a)
    print(f"{mx:.03f}, {mn:.03f}")
