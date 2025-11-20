N = input(int())
r = 0
for i in range(N):
    a = int(input("Enter the base value:"))
    b = int(input("Enter the potency of base:"))
    r = (pow(a,b))%10
    print(r)