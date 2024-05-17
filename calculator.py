def add(x,y):
    result = x+y
    return result

def subtract (a,b):
    result = b-a
    return result

def divide (c,d):
    result = d/c
    return result

def multiply (e,f):
    result = e*f
    return result

def remainder(g,h):
    result = g%h
    return result

def power_of(i,j):
    result = i**j
    return result


#A function that accepts any number of arguments
def sum(*numbers):
    total=0
    for number in numbers:
        total+=number
    return total



def multiply_many(*numbers):
    total=1
    for number in numbers:
        total*=number
    return total


#A function that accepts any number of keyword arguments

#We add ** before a parameter name


def sum_and_greet(*args, **kwargs):
    total = 0
    for x in args:
        total+=x

    f = kwargs["first_name"]
    l=kwargs["last_name"]
    greeting = f"Hello {f} {l} the sum of your numbers is {total}"
    return greeting



def greetings(name,age):
    print(f"Hello my name is {name} and I was born in {2024-age}")


def addition(integers):
    sum = 0
    for x in integers:
     sum +=x
     return sum

    