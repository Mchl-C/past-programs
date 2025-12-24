import sympy as sp

# Define symbols
x, y = sp.symbols('x y')

# Indefinite integral
indefinite_integral = sp.integrate(sp.sin(x), x)

# Definite integral
definite_integral = sp.integrate(sp.sin(x), (x, 0, sp.pi))

print(f"Indefinite Integral: {indefinite_integral}")
print(f"Definite Integral: {definite_integral}")

# Sympy supports exact arithmetic with fractions
fraction_result = sp.Rational(3, 7) + sp.Rational(2, 5)
print(f"Fraction Result: {fraction_result}")

import sympy.plotting as syp

# Plot a function
syp.plot(x**2 - 4, (x, -3, 3), title="y = x^2 - 4", xlabel="x", ylabel="y")
