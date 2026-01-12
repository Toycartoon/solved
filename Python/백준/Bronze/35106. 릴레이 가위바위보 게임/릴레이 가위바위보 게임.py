n = int(input())
a = list(map(int, input().split()))

ans = [a.count(1), a.count(2), a.count(3)]
print(ans.index(min(ans))+1)
print(ans.index(max(ans))+1)
