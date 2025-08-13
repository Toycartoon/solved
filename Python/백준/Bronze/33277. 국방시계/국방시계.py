from math import trunc

n, m = map(int, input().split())
x = trunc(1440 * m / n)
print(f"{str(x // 60).zfill(2)}:{str(x % 60).zfill(2)}")
