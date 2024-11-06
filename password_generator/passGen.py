import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = 0
nr_symbols = 0
nr_numbers = 0
atempt = False

password_list = []


sum = 0

while sum < 8:
    if sum < 8 and atempt:
        print("Pleas give 8 char min")

    atempt = True
    print("Welcome to the PyPassword Generator!")
    print("The minimum lenght is 8 ements")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    sum = nr_letters + nr_symbols + nr_numbers


for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0,nr_numbers):
    password_list.append(random.choice(numbers))

print("Symbols")
print(password_list)

random.shuffle(password_list)

password =""

for i in password_list:
    password = password + i

print("Generated pass")
print(password)