n = int(input())
e, i, o = 0, 0, 0
for x in range(n):
    s = input()
    if "black" in s and "blue" in s:
        e += 1
    elif "white" in s and "gold" in s:
        i += 1
    else:
        o += 1

print(e / n * 100)
print(i / n * 100)
print(o / n * 100)
