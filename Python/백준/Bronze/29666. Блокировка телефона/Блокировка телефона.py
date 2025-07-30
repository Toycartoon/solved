s = {123, 456, 789, 147, 258, 369, 58}
if int("".join(sorted([*input()]))) in s:
    print("Unlocked")
else:
    print("Locked")
