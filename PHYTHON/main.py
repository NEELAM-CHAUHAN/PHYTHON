# print("Namaste Neelam!! Welcome to Phython course.")
# a = 10
# print(a)
# num1 = int(input("Enter the first no. : "))
# num2 = int(input("Enter the second no. : "))
 
# if num1 > num2:
#   print(f"{num1} is greater than {num2}")
# elif num2 > num2:
#   print(f"{num2} is greater than {num1}")
# else:
#   print("Both the number are same")

# gen= input("please tell your gender as character (M OR F ):-")
# if gen =='M'or gen =='m':
#    print ("GOOD MORNING SIR")
# elif gen =='F' or gen =='f':
#   print("GOOD MORNING MAM")
# else:
#   print("invalid input check it again")

# num = int(input("please tell your number :-"))
# if num%2 == 0:
#   print("even number")
# else:
#   print("odd number")
 
# name = input("please tell your name : ")
# age = int(input("now tell your age :- "))
# take = 18 -age
# if age >= 18:
#   print(f" hello {name} you are eligible for voting ")
# else:
#   print(f" hello {name} you are not eligible for voting. You have {take} year to vote")

# year = int(input("tell your year :-"))
# if year %100 == 0 and year%400 ==0:
#   print("its a leap year")
# elif year%100 != 0 and year%4 ==0:
#   print("its not a leap year")
# else:
#   print("its a normal year")
  
a ="ssf84593@#%&"
char = 0
digit = 0
spchar = 0
for i in a:
  if i.isdigit():
    digit+=1
  elif  i.isalpha():
    char+=1
  else:
    spchar+=1
print(f"your digits {digit} your alphatbets {char} and your special character {spchar}")



   
  
 
