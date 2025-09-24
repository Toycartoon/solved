s = input().split()
ns = []
for i in s:
    if i not in ("bubble", "tapioka"):
        ns.append(i)
print(*ns if len(ns) > 0 else ["nothing"])
