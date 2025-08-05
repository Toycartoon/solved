w = input()
s = input()

arr = []
for i in w:
    if i not in arr:
        arr.append(i)

for i in range(65, 91):
    if chr(i) not in arr:
        arr.append(chr(i))

for i in s:
    print(arr[ord(i)-65], end="")
