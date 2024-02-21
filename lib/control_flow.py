#!/usr/bin/env python3

def admin_login(username, password):
    return "Access denied" if (username != "admin" and username != "ADMIN") or password != "12345" else "Access granted"
    

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature > 40 and temperature < 65:
        return "It's a little chilly out there!" 
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"


def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
    

def calculator(operation, num1, num2):
    operations = {
        "+" : num1 + num2,
        "-" : num1 - num2,
        "*" : num1 * num2,
        "/" : num1 / num2
    }

    result = operations.get(operation)

    if result == None:
        print("Invalid operation!")
        return None
    
    return result
    