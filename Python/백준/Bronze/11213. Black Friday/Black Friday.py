n = int(input())
a = list(map(int, input().split()))

for i in range(6, 0, -1):
    if a.count(i) == 1:
        print(a.index(i)+1)
        exit()
print("none")
