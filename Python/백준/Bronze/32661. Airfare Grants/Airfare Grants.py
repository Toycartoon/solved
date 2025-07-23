n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
print(abs(min(max(a) // 2, min(a)) - min(a)))
