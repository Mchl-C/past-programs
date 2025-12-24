import sympy as sp

# Define symbols
x, y = sp.symbols('x y')

# --------------------------------------------------------------------
# Main Code

while True:
    n = input("Input equation : ")
    r = input("range : ").split()

    if n == 'quit' : break
    if r[0] == '-' : r = False
    else : r[0], r[1] = sp.rad(int(r[0])), sp.rad(int(r[1]))
    
    # Convert to sympy eq
    user_input = sp.sympify(n)

    try:
        expr = sp.sympify(user_input, locals={'sqrt': sp.sqrt})
        print("Expression : ")
        print(sp.pretty(expr))
        print()
        print()
        
        # Simplify, factorise
        rationalized_expr = sp.together(expr)
        simplified_expr = sp.simplify(rationalized_expr)
        print("Simplified : ")
        print(sp.pretty(simplified_expr))
        print()
        print()
        
        factorised_expr = sp.factor(simplified_expr)
        print("Factorised : ")
        print(sp.pretty(factorised_expr))
        print()
        print()
        
        # Integrate the expression
        if r : integral = sp.simplify(sp.integrate(factorised_expr, (x, r[0], r[1])))
        else : integral = sp.simplify(sp.integrate(factorised_expr, (x)))
        print("Integral: ")
        print(sp.pretty(integral))
        print()

    except (sp.SympifyError, SyntaxError):
        print("Invalid input. Please check your equation.")

