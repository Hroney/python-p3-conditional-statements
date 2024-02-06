#!/usr/bin/env python3

def admin_login(username, password):
    adminPass = True if (username.lower() == 'admin') else False
    passwordPass = True if password == '12345' else False
    return 'Access granted' if (passwordPass and adminPass) else 'Access denied'
     

def hows_the_weather(temperature):
    if temperature > 85: 
        return "It's too dang hot out there!"
    elif temperature < 40:
        return "It's brisk out there!"
    elif temperature < 65 and temperature > 40:
        return "It's a little chilly out there!"
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
    calc_dict = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1 / num2,
    }
    returnMessage = calc_dict.get(operation, None)
    if returnMessage == None:
        print("Invalid operation!")
    return returnMessage
