n = bin(int(input()))[2:].zfill(32)
s = ""
for i in n:
    if i == "0":
        s += "1"
    else:
        s += "0"
tmp = bin(int(s, 2)+1).zfill(32)[2:][-32:]
ans = 0
for i in range(32):
    if n[i] != tmp[i]:
        ans += 1
print(ans)
