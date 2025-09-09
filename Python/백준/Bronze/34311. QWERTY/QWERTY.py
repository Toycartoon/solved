w = "qwertyuiopasdfghjklzxcvbnm"
n = int(input())
s = input()
for i in s:
    if i.isalpha():
        print(w[ord(i)-97], end="")
    else:
        print(i, end="")
