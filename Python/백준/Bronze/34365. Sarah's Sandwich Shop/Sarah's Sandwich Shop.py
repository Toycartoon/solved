w = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]
for t in range(int(input())):
    s = input()
    for i in s.lower():
        print(w[ord(i)-97], end="")
    print()
