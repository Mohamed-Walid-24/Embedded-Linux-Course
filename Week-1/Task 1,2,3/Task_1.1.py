# Task_1.1
# Write a Python program to count the number 4 in a given list.

data = input("Enter your list: ")
data = data.split()
n_data = []

for i in data:
    try:
        n_data.append(int(i))
    except:
        pass
#print(n_data)
print("4 is repeated: ",n_data.count(4)," times")