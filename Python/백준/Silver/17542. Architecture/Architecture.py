r, c = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

if max(x) == max(y):
    print("possible")
else:
    print("impossible")
