n = int(input())
m = int(input())
a = list(map(int, input().split()))

s = [0 for _ in range(n)]
for i in a:
    v = list(map(int, input().split()))
    for x in range(len(v)):
        if v[x] != i:
            s[i-1] += 1
        else:
            s[x] += 1

for i in s:
    print(i)
