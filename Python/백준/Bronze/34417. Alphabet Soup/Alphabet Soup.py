w = [False for _ in range(26)]
l = input()
for i in l:
    w[ord(i)-65] = True

if w.count(True) == 26:
    print("Alphabet Soup!")
else:
    for i in range(26):
        if not w[i]:
            print(chr(i+65), end="")
