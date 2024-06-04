num = input("Enter Number: ")
x = 0
for i in num:
    if int(i) % 2 == 0:
        x += int(i)

print("Sum of even numbers:", x)