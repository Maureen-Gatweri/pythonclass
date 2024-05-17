def print_numbers(n):
    numbers = range(n)
    for number in numbers:
        print(number)


def print_even_numbers(n):
    numbers = range(n)
    for number in numbers:
        if number % 2==0:
            print(number) 


def odd_or_even(n):
    numbers = range(n)
    for number in numbers:
        if number % 2 ==0:
            print(f"{number} is even")   
        else:
            print(f"{number} is odd")    


# *Elif Statement
# Elif statement allows us to do more than one comparison.

def check_divisibility(n):
    numbers = range(n)
    for number in numbers:
        if number %3 == 0:
            print(f"{number} is divisible by 3")
        elif number%5==0:
            print(f"{number} is divisible by 5")
        elif number %7 ==0:
            print(f"{number} is divisible by 7")
        else:
            print(f"{number} is not divisible by 3,5 or 7")

def count_down(n):
    x = 0
    while n >x:
           print(n)
           n-=1

def count_down_to_five(n):
    x = 0
    while n>x:
     
        if n == 5:
          break
        n-=1
        print(n)


# Continue statement

# It skips the remainder of the current iteration and jumps to the next iteration of the while loop


def divisible_by_seven(n):
    x = 1
    while x<=n:
        x+=1
        if x% 7!=0:
           continue
        print(f"{x} is divisible by 7")
      
      
# Using while, continue and if statements, 
# Write a function that prints all the odd numbers between 0 and 100
        
# Create a function named Fizzbuz which does the following:
        # for numbers divisible by 3 it prints 'fizz'
        # for numbers divisible by 5  it prints buzz
        # For al the other numbers it prints fizzbuzz

def print_fizzbuzz(x):
    numbers = range(x)
    for number in numbers:
        if number % 3 == 0:
            print(f"Fizz")
        elif number%5 ==0:
            print(f"Buzz")
        else:
            print(f"Fizzbuzz")


def check_odd_numbers():
   
    x = 1
    while x<100:
        x+=1
        if x %2 ==0:
            continue
        print(f"{x} is an odd number")
