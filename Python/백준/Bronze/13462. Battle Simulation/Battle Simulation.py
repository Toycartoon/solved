s = [*input()]
idx = 0
while idx < len(s):
    if idx + 2 < len(s) and s[idx] != s[idx+1] != s[idx+2] != s[idx]:
        print("C", end="")
        idx += 2
    else:
        if s[idx] == "R":
            print("S", end="")
        elif s[idx] == "B":
            print("K", end="")
        elif s[idx] == "L":
            print("H", end="")
    idx += 1
