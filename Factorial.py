num = int(input("Enter Number: "))
fact = 1

if num<0:
    print("Sorry, Factorial of negetive numbers can't be calculated!!!")
elif num==0:
    print(f"Factorial of {num} is: 0")
else:
    for i in range(1,num+1):
        fact = fact*i
    print(f"Factorial of {num} is: {fact}")
