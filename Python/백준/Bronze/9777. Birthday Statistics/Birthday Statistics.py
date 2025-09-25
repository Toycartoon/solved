a = [0 for _ in range(12)]
for t in range(int(input())):
    i, s = input().split()
    d, m, y = map(int, s.split("/"))
    a[m-1] += 1

for i in range(12):
    print(i+1, a[i])
