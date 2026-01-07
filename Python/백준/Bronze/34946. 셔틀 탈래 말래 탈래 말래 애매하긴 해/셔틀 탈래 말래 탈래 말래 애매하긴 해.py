a, b, c, d = map(int, input().split())

if a + b <= d and c <= d:
    print("~.~")
elif a + b <= d:
    print("Shuttle")
elif c <= d:
    print("Walk")
else:
    print("T.T")
