n = int(input())
w = list(map(int, input().split()))

w.sort()
a = []
for i in range(n):
    a.append(w[i] + w[-i-1])
print(min(a))
