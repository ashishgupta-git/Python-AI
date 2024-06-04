import os


#   ---- CREATING FOLDERS ----

# if(not os.path.exists("data")):
#     os.mkdir("data")

# for i in range(0, 200):
#     os.mkdir(f"data/day{i+1}")


    # ---- REANAMING FOLDERS ----

# for i in range(0, 200):
#     os.rename(f"data/day {i+1}", f"data/waw {i+1}")


    #-----VIEW FOLDERS IN FOLDER----

folders = os.listdir("data")

print(folders)

for i in folders:
    print(i)
