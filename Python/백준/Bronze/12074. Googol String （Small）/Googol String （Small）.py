s = "0"
while len(s) < 100000:
    a = ""
    for i in s[::-1]:
        if i == "0":
            a += "1"
        else:
            a += "0"
    s = s + "0" + a

for t in range(int(input())):
    k = int(input())
    print(f"Case #{t+1}: {s[k-1]}")
