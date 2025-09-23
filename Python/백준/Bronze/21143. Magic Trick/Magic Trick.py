a = [0 for _ in range(26)]
s = input()
for i in s:
    a[ord(i)-97] += 1
print(int(not max(a) > 1))
