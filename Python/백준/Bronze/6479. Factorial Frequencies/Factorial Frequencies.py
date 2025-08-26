from math import factorial as f

while True:
    n = int(input())
    if n == 0:
        break

    _ = input()
    s = str(f(n))
    print(f"{n}! --")
    print(f"   (0){str(s.count("0")).rjust(5)}    (1){str(s.count("1")).rjust(5)}    (2){str(s.count("2")).rjust(5)}    (3){str(s.count("3")).rjust(5)}    (4){str(s.count("4")).rjust(5)} ")
    print(f"   (5){str(s.count("5")).rjust(5)}    (6){str(s.count("6")).rjust(5)}    (7){str(s.count("7")).rjust(5)}    (8){str(s.count("8")).rjust(5)}    (9){str(s.count("9")).rjust(5)} ")
