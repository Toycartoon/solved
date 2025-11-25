x, y = map(int, input().split())
for i in range(int(input())):
    a, b = map(int, input().split())
    if a == x or b == y:
        print(0)
    else:
        print(1)
