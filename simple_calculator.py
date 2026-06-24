num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("choose an operation (+, -, *, /): ")
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0:
       result = num1 / num2
       print(f"{num1} / {num2} = {result}")
    else:
        print("Error: cannot divide by zero.")
else:
    print("Error: Ivalid operation.")
word = input("Enter a word: ")
print(f"Length of the word: {len(word)}")
print(f"Uppercase: {word.upper()}")
print(f"Repeated 3 times: {word * 3}")
