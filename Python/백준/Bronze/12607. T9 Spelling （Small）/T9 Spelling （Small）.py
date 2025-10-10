w = ["2", "22", "222", "3", "33", "333", "4", "44", "444", "5", "55", "555", "6", "66", "666", "7", "77", "777", "7777",
     "8", "88", "888", "9", "99", "999", "9999"]
for t in range(int(input())):
    s = input()
    a = []
    for i in s:
        if i.isalpha():
            if len(a) > 0 and a[-1][0] == w[ord(i)-97][0]:
                a.append(" ")
            a.append(w[ord(i)-97])
        else:
            if len(a) > 0 and a[-1][0] == "0":
                a.append(" ")
            a.append("0")
    print(f"Case #{t+1}: ", end="")
    print(*a, sep="")
