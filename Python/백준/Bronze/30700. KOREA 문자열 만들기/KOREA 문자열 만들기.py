x = "KOREA"
s = input()
idx = 0
for i in s:
    if i == x[idx % 5]:
        idx += 1

print(idx)
