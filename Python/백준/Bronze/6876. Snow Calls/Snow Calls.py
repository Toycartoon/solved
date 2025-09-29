w = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
for t in range(int(input())):
    a = input().replace("-", "")
    s = ""
    for i in a:
        if i.isdigit():
            s += i
        elif i.isupper():
            s += str(w[ord(i)-65])
    print(f"{s[:3]}-{s[3:6]}-{s[6:10]}")
