import sys

n = 1
user_input = input("pick a max number for fizz buzz!!! ")
user_input = int(user_input)
print(user_input)

for num in range(1, user_input):
    if (n % 3 == 0):
        print("fizz")
    elif (n % 5 == 0 and n % 3 == 0):
        print("fizz buzz")
    elif (n % 5 == 0):
        print("buzz")

    else:
        print(n)
    n += 1;