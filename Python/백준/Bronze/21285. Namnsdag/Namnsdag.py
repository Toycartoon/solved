s = input()
for i in range(int(input())):
    v = input()
    if len(v) != len(s):
        continue

    diff = 0
    for j in range(len(v)):
        if v[j] != s[j]:
            diff += 1

    if diff <= 1:
        print(i+1)
        break
