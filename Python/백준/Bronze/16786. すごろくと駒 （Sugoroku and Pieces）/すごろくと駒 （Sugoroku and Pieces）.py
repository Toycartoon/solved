n = int(input())
x = list(map(int, input().split()))
m = int(input())
a = list(map(int, input().split()))
for i in a:
    if x[i-1] + 1 not in x and x[i-1] + 1 < 2020:
        x[i-1] += 1

for i in x:
    print(i)
