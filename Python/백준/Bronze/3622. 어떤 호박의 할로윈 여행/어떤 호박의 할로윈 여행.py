A, a, B, b, p = map(int, input().split())
if A > B:
    A, a, B, b = B, b, A, a

if A + B <= p or (A <= b and B <= p):
    print("Yes")
else:
    print("No")
