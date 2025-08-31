a = bin(int(input()))
b = bin(int(input()))
c = bin(int(input()))
print(str(int(a[2:][-4:].zfill(4)+b[2:][-4:].zfill(4)+c[2:][-4:].zfill(4),2)).zfill(4))
