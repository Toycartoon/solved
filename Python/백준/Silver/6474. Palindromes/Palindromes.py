w = {"A": "A", "E": "3", "H": "H", "I": "I", "J": "L", "L": "J", "M": "M", "O": "O", "S": "2", "T": "T", "U": "U",
     "V": "V", "W": "W", "X": "X", "Y": "Y", "Z": "5", "1": "1", "2": "S", "3": "E", "5": "Z", "8": "8"}
while True:
    try:
        s = input()
        f = True
        m = ""
        for i in s:
            if i not in w:
                f = False
                break
            m += w[i]

        if not f:
            if s == s[::-1]:
                print(f"{s} -- is a palindrome.")
            else:
                print(f"{s} -- is not a palindrome.")
        else:
            if m == m[::-1]:
                print(f"{s} -- is a mirrored palindrome.")
            else:
                print(f"{s} -- is a mirrored string.")
        print()
    except EOFError:
        break