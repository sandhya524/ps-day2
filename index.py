# Print all numbers from 1 to 100 using a for loop.
for i in range(1,101):
    print(i)

# # Write a program to print the sum of the first n natural numbers. (n*n+1/ 2)
n = int(input("enter a nutural num: "))
sum = 0
for j in range(1,n+1):
    sum += j 
print(sum)   

# Print all even numbers between 1 and 50 using a while loop
numbers = 1
while numbers < 52:
    if numbers % 2 == 0:
        print(numbers,"is even")
    numbers += 1         

# Write a program to display the multiplication table of a given number. First 20 
user_mul = int(input("enter a multiplication num: "))
mul = 1
for m in range(1,11):
    mul = user_mul * m
    print(f"{user_mul}*{m}={mul}") 

# Write a program to calculate the factorial of a number using a while loop.
facto = int(input('enter a number to factorial: '))
mul1 = 1
while facto != 0:
      mul1 = mul1 * (facto)
      facto -= 1
print(mul1)      

# Print all numbers from 1 to 100 that are divisible by 3 and 5 using a for loop.

for l in range(1,101):
    if l % 5 == 0:
        print(l,"is divisible by 5")
    elif l % 3 == 0:
        print(l, "divisible by 3")  
    else:
        print(l,"is not divisible by 3 and 5")      


        