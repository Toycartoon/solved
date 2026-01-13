n = int(input())
ans = 0
while n != 0:
    n = int(bin(n)[2:][::-1], 2)-1
    ans += 1
print(ans)
