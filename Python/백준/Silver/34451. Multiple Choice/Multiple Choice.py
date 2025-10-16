n = int(input())
a = [input() for _ in range(n)]

v = []
for _ in range(int(input())):
    id = int(input())
    ans = 0
    for i in a:
        s = input()
        if s == i:
            ans += 1
    v.append((id, ans))

t = input()
if t == "STUDENT_ID_ASC":
    v.sort(key=lambda x: x[0])
elif t == "STUDENT_ID_DESC":
    v.sort(key=lambda x: -x[0])
elif t == "GRADE_ASC":
    v.sort(key=lambda x: (x[1], x[0]))
elif t == "GRADE_DESC":
    v.sort(key=lambda x: (-x[1], x[0]))

for i in v:
    print(*i)
