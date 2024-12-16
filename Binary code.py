# Input: Decimal number
decimal = int(input("Enter a decimal number: "))

# Initialize variables
binary = ""  # To store the binary result
number = decimal  # Copy of the input number for processing

# Edge case for 0
if number == 0:
    binary = "0"

# Convert decimal to binary
while number > 0:
    remainder = number % 2  # Get the remainder when divided by 2
    binary = str(remainder) + binary  # Add the remainder to the front of the binary string
    number = number // 2  # Update the number by integer division

# Display the result
print(f"The binary representation of {decimal} is: {binary}")