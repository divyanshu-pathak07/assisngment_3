#finding factorial with function
a = int(input('Enter the number :')) #taking input

def fact(a): #function

  if a < 2: #if a = 1 it will return 1
   return 1

  else:
    return a*fact(a-1) #using recursion
result = fact(a)
print(f"factorial of {a} is {result}")