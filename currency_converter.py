with open('currency.txt') as f:
    lines=f.readlines()
exchng={}
for line in lines:
    parsed=line.split("\t")
    exchng[parsed[0]]=parsed[1]

amount=int(input("enter your Amount: \n"))
print("enter currency name as listed below: \n")
[print(item) for item in exchng.keys()]
currency=input("enter the currency Name: \n")
print(f"{amount} INR is == {amount*float(exchng[currency])} {currency}")
