from itertools import product as prod

s = input().split("?")
for i in prod(["==", "+", "-", "*"], repeat=3):
    x = s[0] + i[0] + s[1] + i[1] + s[2] + i[2] + s[3]

    if eval(x) and x.count("==") == 1:
        print(x.replace("==", "="))
        exit()

print("EI SAA")
