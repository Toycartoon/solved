a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

print(int(a1 * n0 + a0 >= c * n0 and a1 >= c))