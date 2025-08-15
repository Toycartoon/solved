n = int(input())
a = list(map(int, input().split()))

s = set(range(min(a), max(a)+1)) - set(a)
print(len(s))
print(*sorted(list(s)))
