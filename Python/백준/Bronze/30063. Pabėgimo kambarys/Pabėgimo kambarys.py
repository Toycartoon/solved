w = {"R": 1, "A": 2, "K": 1, "T": 1, "S": 1}
n = int(input())
s = input()
for i in range(n):
    if s[i] in w:
        w[s[i]] -= 1
        if w[s[i]] == 0:
            del w[s[i]]

    if len(w) == 0:
        print(i+1)
        break
