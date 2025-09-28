a = int(input())
b = int(input())

double = set()
triple = set()
i = 1
while i ** 2 <= b:
    if a <= i ** 2 <= b:
        double.add(i ** 2)
    i += 1

i = 1
while i ** 3 <= b:
    if a <= i ** 3 <= b:
        triple.add(i ** 3)
    i += 1

print(len(double & triple))
