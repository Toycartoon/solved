n = int(input())
h = list(map(int, input().split()))
w = list(map(int, input().split()))

a = 0
for i in range(n):
    a += (h[i] + h[i+1]) * w[i] / 2
print(a)
