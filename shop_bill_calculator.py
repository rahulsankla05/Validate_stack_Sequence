# shop_bill_calculator.py
Sum=0
while(True):
    user_Input=input("Enter the item Price or press q to quit: \n")
    if user_Input!="q":
        Sum+=int(user_Input)
        print(f"Your bill so far is: ")
    else:
        print(f"*Thanks for shopping with us*, Total Pay is {Sum} :")
        break

