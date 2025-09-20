f = True
n = int(input())
for i in range(n):
    if int(input()) < 48:
        f = False
        break
print(f)