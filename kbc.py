questions = [
    ["Best Captain of Indian Cricket Team? ", "Virat Kohli", "Rohit Sharma", "MS Dhoni","None of the above", 3],
    ["Opeanor of Indian Cricket Team? ", "Virat Kohli", "Rohit Sharma", "MS Dhoni","None of the above", 1],
    ["Leader of Indian Cricket Team? ", "Virat Kohli", "Rohit Sharma", "MS Dhoni","None of the above", 3],
    ["Present Captain of Indian Cricket Team? ", "Virat Kohli", "Rohit Sharma", "MS Dhoni","None of the above", 2],
    ["Wicket keeper of Indian Cricket Team? ", "Virat Kohli", "Rohit Sharma", "MS Dhoni","None of the above", 3],
    ["Best Opeanor of Indian Cricket Team? ", "Virat Kohli", "Rohit Sharma", "MS Dhoni","None of the above", 1],
    ["Present Captain of Indian Cricket Team? ", "Virat Kohli", "Rohit Sharma", "MS Dhoni","None of the above", 1],
    ["Captain of Indian Football Team? ", "Virat Kohli", "Rohit Sharma", "MS Dhoni","None of the above", 2],
    ["Best Captain of Indian Cricket Team? ", "Virat Kohli", "Rohit Sharma", "MS Dhoni","None of the above", 4],
    ["Best Captain of Indian Cricket Team? ", "Virat Kohli", "Rohit Sharma", "MS Dhoni","None of the above", 3],
    ["Best Captain of Indian Cricket Team? ", "Virat Kohli", "Rohit Sharma", "MS Dhoni","None of the above", 3],
]

levels = [1000,2000,3000,4000,10000,20000,30000,40000,80000,160000,320000]

money =0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"Question for Rs. {levels[i]}")
    
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")
reply = int(input("Enter Your Option[1-4]:"))
if reply==question[-2]:
    print(f"Correct Answer, you won Rs. {levels[i]}")
    if (i == 4):
        money =10000
    
    elif (i == 9):
        money = 320000
    elif (i == 14):
        money = 10000000
else:

print("wrong")

        
print(f"Yor take home money is {money}")





# questions = [
#     ["Best Captain of Indian Cricket Team? ", "Virat Kohli", "Rohit Sharma", "MS Dhoni","None of the above", 3],
#     ["Opener of Indian Cricket Team? ", "Virat Kohli", "Rohit Sharma", "MS Dhoni","None of the above", 1],
#     ["Leader of Indian Cricket Team? ", "Virat Kohli", "Rohit Sharma", "MS Dhoni","None of the above", 3],
#     ["Present Captain of Indian Cricket Team? ", "Virat Kohli", "Rohit Sharma", "MS Dhoni","None of the above", 2],
#     ["Wicket keeper of Indian Cricket Team? ", "Virat Kohli", "Rohit Sharma", "MS Dhoni","None of the above", 3],
#     ["Best Opener of Indian Cricket Team? ", "Virat Kohli", "Rohit Sharma", "MS Dhoni","None of the above", 1],
#     ["Present Captain of Indian Cricket Team? ", "Virat Kohli", "Rohit Sharma", "MS Dhoni","None of the above", 1],
#     ["Captain of Indian Football Team? ", "Virat Kohli", "Rohit Sharma", "MS Dhoni","None of the above", 2],
#     ["Best Captain of Indian Cricket Team? ", "Virat Kohli", "Rohit Sharma", "MS Dhoni","None of the above", 4],
#     ["Best Captain of Indian Cricket Team? ", "Virat Kohli", "Rohit Sharma", "MS Dhoni","None of the above", 3],
#     ["Best Captain of Indian Cricket Team? ", "Virat Kohli", "Rohit Sharma", "MS Dhoni","None of the above", 3],
# ]

# levels = [1000, 2000, 3000, 4000, 10000, 20000, 30000, 40000, 80000, 160000, 320000]

# money = 0
# for i in range(len(questions)):
#     question = questions[i]
#     print(f"Question for Rs. {levels[i]}")
    
#     print(f"a. {question[1]}")
#     print(f"b. {question[2]}")
#     print(f"c. {question[3]}")
#     print(f"d. {question[4]}")
    
#     reply = int(input("Enter Your Option [1-4]: "))
#     if reply == question[-1]:
#         print(f"Correct Answer! You won Rs. {levels[i]}")
#         if i == 4:
#             money = 10000
#         elif i == 9:
#             money = 320000
#         elif i == 10:
#             money = 10000000
#         else:
#             money += levels[i]
#     else:
#         print("Wrong Answer!")
#         break

# print(f"Your take-home money is Rs. {money}")
