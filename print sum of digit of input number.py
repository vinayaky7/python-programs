#print sum of digit of input number
num=int(input("Enter any number"))
s=0
while num>0:
    r=num%10
    s=s+r
    num=num//10

print(f"sum of digit of number {s}")
