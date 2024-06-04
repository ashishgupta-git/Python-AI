x = input("Enter a word:")
y = len(x)

for i in range(0,x):
    for j in range(0,i):
        print(x[j], end="")
print(y[i], end="")