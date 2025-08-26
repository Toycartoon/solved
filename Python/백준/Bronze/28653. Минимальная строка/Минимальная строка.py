a = input()
b = input()

s = [*a] + [*b]
s.sort()
print("".join(s[:len(a)]))
