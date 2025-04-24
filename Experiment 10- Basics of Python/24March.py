# conditional statements

# num = int(input("Enter a number: ")) 
# if num > 0: 
#     print("Positive number") 
# elif num < 0: 
#     print("Negative number") 
# else: 
#     print("Zero")

# loops
# for loop
# for i in range(5):
#     print(i)


# while loop
count = 0 
# while count < 5: 
#     print(count, end=" ") 
#     count += 1


#WAP IN PYTHON TO PRINT CHARACTERS OF A STRING
# s=input("Enter a string: ")
# for i in range(len(s)):
#     print (s[i])


#Wap in python to print sum of digits of a number entered by the user
# n=int(input("Enter a number: "))
# sum=0
# while(n>0):
#     d=n%10
#     sum+=d
#     n=n//10
# print("The sum of number is: ", sum)


# Fahrenheit to Celsius
# tempF=int(input("Enter temperature in Fahrenheit: "))
# tempC=(5/9)*(tempF-32)
# print("The temperature in Celsius is: ", tempC)
# # Celsius to Fahrenheit
# tempC2=int(input("Enter temperature in Celsius: "))
# tempF2=(9/5)*(tempC2)+32
# print("The temperature in Fahrenheit is: ", tempF2)

# patterns
# print the following pattern:
# A 
# A A 
# A A A 
# A A A A 
# n=4
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print('A', end=" ")
#     print()


# print the following pattern:
# A 
# A B 
# A B C 
# A B C D 
# n=4
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(chr(65+j-1), end=" ")
#     print()

# WAP IN PYTHON TO COUNT  CHARACTERS OF A STRING
# s=input("Enter a string: ")
# sum=0
# for i in range(len(s)):
#     if(s[i].isalpha()):
#         sum+=1
# print("The number of characters in given string is: ", sum)