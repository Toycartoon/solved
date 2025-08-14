a = []
b = []
for i in range(3):
    a.append(len(input().strip()))

for i in range(3):
    b.append(len(input().strip()))

print("Latitude", ":".join(map(str, a)))
print("Longitude", ":".join(map(str, b)))
