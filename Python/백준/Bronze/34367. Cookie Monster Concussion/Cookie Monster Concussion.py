c = input()
while len(str(c)) > 1:
    c = sum(map(int, [*str(c)]))
print(c)