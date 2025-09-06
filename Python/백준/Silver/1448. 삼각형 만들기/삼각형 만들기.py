import sys

input = sys.stdin.readline

a = []
for i in range(int(input())):
    a.append(int(input()))

a.sort(reverse=True)
f = True
for i in range(len(a)-2):
    if a[i] < a[i+1] + a[i+2] and a[i+1] < a[i] + a[i+2] and a[i+2] < a[i] + a[i+1]:
        f = False
        print(sum(a[i:i+3]))
        break

if f:
    print(-1)
