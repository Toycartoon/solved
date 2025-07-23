c = float(input())
ans = 0
for i in range(int(input())):
    w, l = map(float, input().split())
    ans += w * l * c

print(ans)
