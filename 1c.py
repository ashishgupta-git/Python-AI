import math

a = int(input("Enter value for a :"))
c = int(input("Enter value for c :"))
b = 10

x = -10 + math.sqrt(b**2 - 4*a*c)
y = 2*a

result = x/y
print(result)