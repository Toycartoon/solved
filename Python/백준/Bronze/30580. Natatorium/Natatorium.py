c = int(input())
m = int(input())
p = list(map(int, input().split()))
p.sort()

for i in p:
    if c % i == 0:
        print(i, c // i)
        break
