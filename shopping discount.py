amount = float(input("Enter Total Amount: "))

if amount>1000 and amount<=5000:
    dis = amount*0.05
    print("You Have Got 5% Discount", amount-dis)
elif amount>5000 and amount<=10000:
    dis = amount*0.10
    print("You Have Got 10% Discount", amount-dis)
elif amount>10000 and amount<=20000:
    dis = amount*0.20
    print("You Have Got 20% Discount", amount-dis)
elif amount>20000 and amount<=30000:
    dis = amount*0.30
    print("You Have Got 30% Discount", amount-dis)
elif amount>30000 and amount<=40000:
    dis = amount*0.50
    print("You Have Got 40% Discount", amount-dis)
else:
    print("No Discount")


