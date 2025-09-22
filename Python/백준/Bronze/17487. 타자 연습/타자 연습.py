w = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
s = input()
ans = [0, 0]
for i in s:
    if i.isupper():
        if ans[0] == ans[1]:
            ans[0] += 1
            ans[1] += 1
        elif ans[0] < ans[1]:
            ans[0] += 2
        else:
            ans[1] += 2
    elif i.isalpha():
        ans[w[ord(i.lower())-97]] += 1
    elif i.isspace():
        if ans[0] <= ans[1]:
            ans[0] += 1
        else:
            ans[1] += 1
print(*ans)
