import sys

input = sys.stdin.readline

n = int(input())
alphabet = [False for _ in range(26)]

word = []
for i in range(n):
    s = input().strip()
    alphabet[ord(s[0])-65] = True
    word.append(s)

for w in word:
    f = True
    for i in w:
        if not alphabet[ord(i)-65]:
            f = False
            break
    if f:
        print("Y")
        exit()
print("N")
