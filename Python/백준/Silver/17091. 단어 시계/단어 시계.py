w_hour = ["twelve", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven"]
w_minute = ["half", "one minute", "two minutes", "three minutes", "four minutes", "five minutes", "six minutes",
          "seven minutes", "eight minutes", "nine minutes", "ten minutes", "eleven minutes", "twelve minutes",
          "thirteen minutes", "fourteen minutes", "quarter", "sixteen minutes", "seventeen minutes", "eighteen minutes",
          "nineteen minutes", "twenty minutes", "twenty one minutes", "twenty two minutes", "twenty three minutes",
          "twenty four minutes", "twenty five minutes", "twenty six minutes", "twenty seven minutes", "twenty eight minutes",
          "twenty nine minutes"]

h = int(input())
m = int(input())
if m > 30:
    h = (h + 1) % 12
    print(f"{w_minute[30 - (m % 30)]} to {w_hour[h]}")
else:
    if m == 0:
        print(f"{w_hour[h % 12]} o' clock")
    else:
        print(f"{w_minute[m % 30]} past {w_hour[h % 12]}")
