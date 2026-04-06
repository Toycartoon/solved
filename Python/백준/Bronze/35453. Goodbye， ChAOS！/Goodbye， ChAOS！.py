w = {232: 2017, 88: 2018, 754: 2019, 29: 2020, 28: 2021, 1015: 2022, 1295: 2023, 1073: 2024, 348: 2025}
for t in range(int(input())):
    n = int(input())
    ans = 1
    for i in range(n):
        ans *= len(input())

    if ans in w:
        print(w[ans])
    else:
        print("Goodbye, ChAOS!")