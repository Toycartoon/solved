n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if len(a) + n == len(b) and b[:len(a)] == a and set(b) == set(a):
    print("YES")
else:
    print("NO")
