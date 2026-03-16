import math, os

question = None
avalible_operations = ["-", "+", "/", "*", "^", "root", "clear screen"]
operator = {
    "1": "-",
    "2": "+",
    "3": "/",
    "4": "*",
    "5": "^",
    "6": "root",
    "7": "clear screen"
}

while True:
    question = "N"
    numb = 1
    for no in avalible_operations:
        print(f"{numb}) {no}")
        numb += 1
    if "num3" in locals():
        question = input("do you wan't to contionue with the last awswer Y/N: ").strip().upper()
        if question == "Y":
            num1 = num3
        else:
            print("ok")

    user_input = input("wich one would you like? ").strip().upper()
    if user_input in operator:
        operation = operator[user_input]
    elif user_input in avalible_operations:
        operation = user_input
    if operation == "clear screen":
        os.system("cls" if os.name == "nt" else "clear")
        continue
    if question != "Y":
        num1 = float(input("please enter first number ").strip().upper())
    
    
   
    if operation != "root":
        num2 = float(input("please enter second number ").strip().upper())
    if operation == "-":
        num3 = num1 - num2
        print(f"{num1} - {num2} = {num3}\n")
    elif operation == "+":
        num3 = num1 + num2
        print(f"{num1} + {num2} = {num3}\n")
    elif operation == "/":
        if num2 == 0:
            num3 = 0
        else:
            num3 = num1 / num2
        print(f"{num1} / {num2} = {num3}\n")
    elif operation == "^":
        num3 = num1 ** num2
        print(f"{num1} to the power of {num2} is {num3}")
    elif operation == "root":
        root = int(input("which root would you like? (2 = square, 3 = cube, etc): "))

        if num1 < 0 and root % 2 == 0:
            print("sorry but you can't enter a negative number for an even root")
            continue

        num3 = num1 ** (1/root)

        print(f"The {root} root of {num1} is {num3}")
    
    else:
        print("sorry but this operation dosn't exist")
