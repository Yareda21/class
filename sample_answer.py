# Command-line calculator using loops and if statements Yared Kebede

# Prompt the user for input
user_input = input("Enter your calculation (e.g., 1234*3456): ")

# Initialize variables
num1 = ""
num2 = ""
operator = ""
operator_found = False

# Loop through each character in the input string
for char in user_input:
    if char in '+-*/':
        operator = char
        operator_found = True
    elif operator_found:
        num2 += char
    else:
        num1 += char

# Convert the numbers to floats for calculation
num1 = float(num1)
num2 = float(num2)

# Perform the operation and store the result
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Error: Invalid operator."

# Display the result
print(f"Result: {result}")

