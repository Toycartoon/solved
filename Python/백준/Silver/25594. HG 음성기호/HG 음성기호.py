w = ["aespa", "baekjoon", "cau", "debug", "edge", "firefox", "golang", "haegang", "iu", "java", "kotlin", "lol", "mips",
     "null", "os", "python", "query", "roka", "solvedac", "tod", "unix", "virus", "whale", "xcode", "yahoo", "zebra"]

ans = []
idx = 0
s = input()

f = True
while idx < len(s):
    x = ord(s[idx])-97
    if w[x] == s[idx:len(w[x])+idx]:
        ans.append(s[idx])
        idx += len(w[x])
    else:
        f = False
        break

if f:
    print("It\'s HG!")
    print(*ans, sep="")
else:
    print("ERROR!")
