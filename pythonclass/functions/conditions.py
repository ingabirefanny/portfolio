def print_numbers(n):
    numbers= range(n)
    for number in numbers:
        print(number)

        # if statement checks if an operation is true or false
def print_even_numbers(n):
    numbers=range(n)
    for number in numbers:
        if number % 2== 0:
            print(number)
       # else sttatement ,you can combine if statement with an optional else statement
        #the else statement is executed if the proceding if statement returned false 

def odd_or_even (n):
    numbers= range(n)
    for number in numbers:
        if number % 2 == 0 :
            print(f"{number} is even")  
        else:
            print(f"{number} is odd" )  

        # elif statement allows us to do more than one comparison

def check_divisibility(n):
    numbers= range(n)
    for number in numbers:
        if number%3==0 :
         print(f"{number} is divisible by 3")
        elif number % 5 == 0 :
            print(f"{number} is divisible by 5")
        elif number % 7 ==0:
            print(f"{number} is divisible by 7")
        else:
            print(f"{number} is not divisible by 3,5,7")        


# While loop continues to iterate as long as the given condition is true


def count_down(n):
    x=0
    while n > x :
        print(n)
        n-=1 
# Break stops the while loop even if the set of condition is true

def count_down_to_five(n):
    x=0
    while n > x:
        print(n)
        if n == 5:
            break
        n-=1
# Continue statement skips the remainder the current iteration and jummps to the next iteration of the while loop

def divisible_by_seven(n):
    x=1
    while x <= n:
        x+=1
        if x % 7!= 0:
            continue
        print(f"{x}is divisible by 7")

# using while ,continue and if statement ,write a function that prints all the odd numbers between 0 and 100
# create a function print fizzbuzz ,for numbers by 3, it prints fizz,for number divisible 5 ,it prints buzz,for numbers divisible by both 3 and 5 ,it prints fizzbuzzt