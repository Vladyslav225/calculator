firstNumber = input("Your first number: ")

if firstNumber.isalpha():
    print("Arithmetic operations are perfomed only with numbers! Bey)))")
    exit()

secondNumber = input("Your second number: ")

if secondNumber.isalpha():
    print("Arithmetic operations are perfomed only with numbers! Bey)))")
    exit()

firstNumber = float(firstNumber)
secondNumber = float(secondNumber)

symbol = input("Select a character (+, -, *, /): ")

if symbol == "+":
    resultAdding = firstNumber + secondNumber
    print(resultAdding)
    print(round(resultAdding, 2))

elif symbol == "-":
    resultSubtraction = firstNumber - secondNumber
    print(resultSubtraction)
    print(round(resultSubtraction, 2))

elif symbol == "*":
    resultIncrease = firstNumber * secondNumber
    print(resultIncrease)
    print(round(resultIncrease, 2))

elif symbol == "/":
    resultDivision = firstNumber / secondNumber
    print(resultDivision)
    print(round(resultDivision, 2))
else:
    print("You should choose a character from the suggested! Bey)))")