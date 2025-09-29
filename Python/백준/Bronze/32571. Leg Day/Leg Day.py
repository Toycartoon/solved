a = []
for i in range(int(input())):
    s = input()
    if "leg" in s:
        a.append("🦵")
    elif "arm" in s:
        a.append("💪")
    else:
        a.append("😴")

for i in range(31):
    if (i-1) // 7 != i // 7:
        if i // 7 != 0:
            print()
        print(i // 7 + 1, end=" ")
    print(a[i % len(a)], end="")
