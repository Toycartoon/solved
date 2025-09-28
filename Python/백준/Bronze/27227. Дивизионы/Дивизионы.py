r = int(input())
s = input()
div = 3 if r <= 1600 else 2 if r <= 1900 else 1
if str(div) in s:
    print(div)
    exit()

for i in s:
    if i == "1":
        print(1)
    elif i == "2":
        if r > 1900:
            print("2*")
        else:
            print(2)
    elif i == "3":
        if r > 1600:
            print("3*")
        else:
            print(3)
