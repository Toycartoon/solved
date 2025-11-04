s = input()

a = [[] for _ in range(26)]
for i in range(int(input())):
    x = input()
    a[ord(x[0])-97].append(x)

f = False
ans = ""
for i in a[ord(s[-1])-97]:
    if i == s:
        continue
    if len(a[ord(i[-1])-97]) == 0 or (len(a[ord(i[-1])-97]) == 1 and s[-1] == i[-1]):
        print(i + "!")
        exit()
    else:
        if not f:
            f = True
            ans = i

if not f:
    print("?")
else:
    print(ans)
