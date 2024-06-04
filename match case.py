age = int(input("Enter Your age: "))

match age:
    case 15:
        print("You can't vote")
    case 16:
        print("You can't vote")
    case 17:
        print("You can't vote")
    case 18:
        print("You can't vote")
    case _:
        print("You can vote")