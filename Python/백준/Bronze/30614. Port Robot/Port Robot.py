n = int(input())
s = input()

f = True
q = []
for i in s:
    if i.isupper():
        if len(q) == 0 or q[-1].upper() != i:
            f = False
            break
        q.pop()
    elif i.islower():
        q.append(i)
print(int(f and len(q) == 0))
