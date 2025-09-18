w = 'HONI'
idx = 0
s = input()
for i in s:
    if i == w[idx % 4]:
        idx += 1
print(idx // 4)
