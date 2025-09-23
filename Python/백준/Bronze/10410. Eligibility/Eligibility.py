for t in range(int(input())):
    name, univ, birth, courses = input().split()
    if int(univ.split("/")[0]) >= 2010 or int(birth.split("/")[0]) >= 1991:
        print(name, "eligible")
    elif int(courses) >= 41:
        print(name, "ineligible")
    else:
        print(name, "coach petitions")
