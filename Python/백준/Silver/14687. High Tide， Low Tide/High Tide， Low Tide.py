n = int(input())
a = list(map(int, input().split()))

a.sort()
l, h = a[:(n+1)//2], a[(n+1)//2:]
l = l[::-1]

for i in range(len(h)):
    print(l[i], end=" ")
    print(h[i], end=" ")

if n % 2 == 1:
    print(l[-1])
