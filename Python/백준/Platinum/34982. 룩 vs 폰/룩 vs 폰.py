n, m, k = map(int, input().split())
if n >= m:
    print(1)
elif n == 1:
    print(2)
elif n == 2 and (m-n > 1 or k-m >= 1):
    print(3)
elif n <= 3:
    print(4)
else:
    print(5)
