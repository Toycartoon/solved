x = "plu"
for t in range(int(input())):
    s = input().lower()
    idx = 0
    for i in s:
        if i == x[idx % 3]:
            idx += 1
    print(idx // 3)
