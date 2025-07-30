n = int(input())
s = input()

if n <= 25:
    print(s)
else:
    if "." not in s[11:-11] or (s[11:-11].count(".") == 1 and (s[11:-11][0] == "." or s[11:-11][-1] == ".")):
        print(s[:11] + "..." + s[-11:])
    else:
        print(s[:9] + "......" + s[-10:])
