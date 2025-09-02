s = input()
for i in range(len(s), 0, -1):
    f = False
    for v in range(i, len(s)+1):
        if s[v-i:v] == s[v-i:v][::-1]:
            f = True
            break

    if f:
        print(i)
        break
