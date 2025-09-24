n = int(input())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(*a-b)