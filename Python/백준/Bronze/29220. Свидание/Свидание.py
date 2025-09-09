k = int(input())
n = int(input())
a = list(map(int, input().split()))
print("YES" if sum(a) - min(a) >= k else "NO")
