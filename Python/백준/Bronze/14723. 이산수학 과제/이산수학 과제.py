n = int(input())

x = 1
d = 0
while d < n:
    x += 1
    d = x * (x - 1) // 2

print(d-n+1, x-1-(d % n))