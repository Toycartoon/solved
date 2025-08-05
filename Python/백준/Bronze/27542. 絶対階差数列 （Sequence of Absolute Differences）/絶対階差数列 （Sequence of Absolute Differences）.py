n = int(input())
a = list(map(int, input().split()))

while len(a) > 1:
    x = []
    for i in range(len(a)-1):
        x.append(abs(a[i] - a[i+1]))
    a = x

print(a.pop())
