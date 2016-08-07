import sys

n = 1

for num in range(1, 101):
    if (n % 3 == 0):
        print("fizz")
    elif (n % 5 == 0 and n % 3 == 0):
        print("fizz buzz")
    elif (n % 5 == 0):
        print("buzz")

    else:
        print(n)
    n += 1;


#while n != 101:
 #   n +=1 
  #  if n / 3:
   #     print("fizz")
#    elif n / 5:
 #       print("buzz")
  #  elif n == 100:
 #       print("Wow that was a lot of numbers!")
 #   else:
 #       print(n)

