w = {"q": 0, "w": 0, "e": 0, "r": 0, "t": 0, "y": 1, "u": 1, "i": 1, "o": 1, "p": 1, "a": 0, "s": 0, "d": 0, "f": 0,
     "g": 0, "h": 1, "j": 1, "k": 1, "l": 1, "z": 0, "x": 0, "c": 0, "v": 0, "b": 0, "n": 1, "m": 1}

while True:
    s = input()
    if s == "#":
        break

    ans = 0
    for i in range(1, len(s)):
        if w[s[i-1]] != w[s[i]]:
            ans += 1

    print(ans)
