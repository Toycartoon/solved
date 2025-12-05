a = []
for i in range(int(input())):
    a.append(input())

if a.index("yonsei") > a.index("korea"):
    print("Yonsei Lost...")
else:
    print("Yonsei Won!")
