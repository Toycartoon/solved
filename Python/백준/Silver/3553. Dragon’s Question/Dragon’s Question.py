n, d = map(int, input().split())
if n < len(str(d)):
    print("No solution")
else:
    print(d * 10 ** (n-len(str(d))))
