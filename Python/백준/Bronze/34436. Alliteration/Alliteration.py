for t in range(int(input())):
    a = input().split()
    w = [0 for _ in range(26)]

    for i in a:
        w[ord(i[0]) - 97] += 1
    print(chr(w.index(max(w))+97))
