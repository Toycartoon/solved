n = int(input())
p = list(map(int, input().split()))
for i in range(1, n):
    if p[i] <= p[0]:
        print(i)
        exit()
print("infinity")
