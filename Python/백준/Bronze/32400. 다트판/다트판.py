d = list(map(int, input().split()))
a = (20 + d[d.index(20)-1] + d[(d.index(20)+1) % 20]) / 3
b = sum(d) / 20
if a < b:
    print("Bob")
elif a > b:
    print("Alice")
else:
    print("Tie")
