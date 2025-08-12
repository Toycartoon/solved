c = input()
a = []
for t in range(int(input())):
    d = input()
    a.append((((int(d[0])-int(c[0]))**2+(int(d[1])-int(c[1]))**2+(int(d[2])-int(c[2]))**2+(int(d[3])-int(c[3]))**2)
              *((int(d[4])-int(c[4]))**2+(int(d[5])-int(c[5]))**2)*((int(d[6])-int(c[6]))**2+(int(d[7])-int(c[7]))**2),
              int(d)))

a.sort(key=lambda x: (-x[0], x[1]))
print(a[0][1])
