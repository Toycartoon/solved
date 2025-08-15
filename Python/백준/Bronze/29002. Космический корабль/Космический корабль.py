n = int(input())
f = list(map(int, input().split()))

s = sum(f)
b = 0
for i in f:
    if s-i == i:
        b = i
    else:
        print(i, end=" ")
print(b)
