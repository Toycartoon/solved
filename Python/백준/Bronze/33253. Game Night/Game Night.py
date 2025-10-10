n = int(input())
a = input()
b = input()

v = [0 for _ in range(26)]
for i in a:
    v[ord(i)-97] += 1

ans = 0
for i in b:
    if v[ord(i)-97] > 0:
        v[ord(i)-97] -= 1
    else:
        ans += 1
print(ans)
