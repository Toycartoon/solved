for t in range(int(input())):
    a, b = input().split()

    print("Ciphertext: ", end="")
    for i in range(len(b)):
        print(chr(65 + ((ord(a[i%len(a)])-65) + (ord(b[i])-65)) % 26), end="")
    print()
