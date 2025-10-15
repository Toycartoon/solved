n = int(input())
s = input().split()
for w in s:
    for i in range(0, len(w)-1, 2):
        v = (ord(w[i])+ord(w[i+1])-194-n) % 26
        print(chr(v+97), end="")
    print(" ", end="")
