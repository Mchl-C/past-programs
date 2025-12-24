import sympy as sp

# Define the variable
x = sp.Symbol('x')

# Take input from the user
user_input = input("Enter the function to integrate: ")

# Convert the string input into a SymPy expression
expr = sp.sympify(user_input)

# Perform the integration
integral_result = sp.integrate(expr, x)

# Print the result
print("The integral is:", integral_result)
