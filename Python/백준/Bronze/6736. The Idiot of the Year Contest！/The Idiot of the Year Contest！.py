from math import factorial as f

for t in range(int(input())):
    a, b = map(int, input().split())
    print(str(f(a)).count(str(b)))
