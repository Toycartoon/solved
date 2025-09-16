a, b = map(int, input().split())

f = True
for e in range(a+1, 63):
    if str(2 ** e)[0] == str(b):
        print(e)
        f = False
        break

if f:
    print(0)
