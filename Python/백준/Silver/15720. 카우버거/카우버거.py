b, c, d = map(int, input().split())
bugi = list(map(int, input().split()))
side = list(map(int, input().split()))
drink = list(map(int, input().split()))
s = sum(bugi + side + drink)

bugi.sort(reverse=True)
side.sort(reverse=True)
drink.sort(reverse=True)
ans = 0
for i in range(min(b, c, d)):
    ans += (bugi[i] + side[i] + drink[i]) * 0.9
ans += sum(bugi[min(b,c,d):] + side[min(b,c,d):] + drink[min(b,c,d):])

print(s)
print(int(ans))
