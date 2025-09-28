s = input().split()
for i in s:
    l, r = 0, len(i)
    for v in i:
        if v == "'":
            l += 2
        else:
            break

    for v in i[::-1]:
        if v == "'":
            r -= 2
        else:
            break
    print(i[l:r], end="")
