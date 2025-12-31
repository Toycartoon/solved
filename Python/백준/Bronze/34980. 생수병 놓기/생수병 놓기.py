n = int(input())
a = input()
b = input()

if a.count("w") > b.count("w"):
    print("Oryang")
elif a.count("w") < b.count("w"):
    print("Manners maketh man")
else:
    if a == b:
        print("Good")
    else:
        print("Its fine")
