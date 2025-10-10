s = input()
k = input()

idx = 0
ans = 0
while idx < len(k):
    ans += 1
    for i in s:
        if i == k[idx]:
            idx += 1
            if idx == len(k):
                break
print(ans)
