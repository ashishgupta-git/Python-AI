num = int(input("Enter your number: "))
print(f"Multiplication table of {num} is: ")

try:
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
except ValueError:
    print("Value Error")
except TypeError:
    print("Type Error")
except NameError:
    print("Name Error")