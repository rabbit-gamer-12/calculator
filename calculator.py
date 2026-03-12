import math, os
question = None
avalible_operations = ["-", "+", "/", "*", "^", "square root", "clear screen"]
operator = {
    "1": "-",
    "2": "+",
    "3": "/",
    "4": "*",
    "5": "^",
    "6": "square root",
    "7": "clear screen"
}

while True:
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
        num1 = int(input("please enter first number ").strip().upper())
    
    
   
    if operation != "square root":
        num2 = int(input("please enter second number ").strip().upper())
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
        print(f"{num1} to the power of{num2} is {num3}")
    elif operation == "square root":
        if num1 < 0:
            print ("sorry but you can't entre a negitive number")
            continue
        num3 = math.sqrt(num1)
        print(f"{num1}'s square root is {num3}")
    
    else:
        print("sorry but this operation dosn't exist")
