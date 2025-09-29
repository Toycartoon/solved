n = int(input())
a = list(map(int, input().split()))

e = 1
for i in a:
    e *= 2
    e -= i
    if e < 0:
        print("error")
        exit()
print(e % 1000000007)
