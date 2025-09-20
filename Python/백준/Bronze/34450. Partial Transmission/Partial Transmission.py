n = int(input())
p = int(input())
print(({*range(p, n+p)} - set(map(int, input().split()))).pop())
