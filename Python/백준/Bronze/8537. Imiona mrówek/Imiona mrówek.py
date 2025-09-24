mx = 0
for i in range(int(input())):
    s = input()
    mx = max(mx, len({*s}))
print(mx)
