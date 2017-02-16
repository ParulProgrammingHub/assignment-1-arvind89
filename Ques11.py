#compound intrest")
a=input("enter the amount")
a=float(a)
b=input("enter the rate")
b=float(b)
c=input("enter the time in year")
p=a*((1+float(b/100))**c)
interest=p-a
print(interest)

