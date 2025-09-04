from fractions import Fraction as f

def v(idx):
    if idx == n-1:
        return a[idx]
    return a[idx] + f(1, v(idx+1))

n = int(input())
a = list(map(int, input().split()))

print(v(0))