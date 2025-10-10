a = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
while True:
    s = input().split()
    if s[0] == "***":
        break
    n = int(input())
    for i in s:
        if i[-1] == "b":
            w = -1
            i = i[:-1]
        elif i[-1] == "#" and i not in a:
            w = 1
            i = i[:-1]
        else:
            w = 0
        print(a[(a.index(i) + n + w) % 12], end=" ")
    print()
