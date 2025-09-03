a = [0, 0, 0, 0, 0, 0, 0, 0]
k = ["1QAZ", "2WSX", "3EDC", "45RTFGVB", "67YUHJNM", "8IK,", "9OL.", "0-=P[];'/"]

s = input()
for i in s:
    for v in range(8):
        if i in k[v]:
            a[v] += 1

for i in a:
    print(i)
