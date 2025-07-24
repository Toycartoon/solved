import sys

sys.setrecursionlimit(10 ** 9)

def f(depth, a, b):
    if depth == 1:
        print(a, b)
        return
    c = 6 - (a + b)
    f(depth-1, a, c)
    print(a, b)
    f(depth-1, c, b)
    return


n = int(input())
print(2 ** n - 1)
if n <= 20:
    f(n, 1, 3)
