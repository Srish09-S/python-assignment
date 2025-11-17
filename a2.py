a = int(input("1et num: "))
b = int(input("2nd num: "))
c = int(input("3rd num: "))
max = "1st num" if (a > b and a > c) else "2nd num" if b > c else "3rd num"
print("Greatest num is: ", max)