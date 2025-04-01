from sympy import symbols, Eq, solve

def balance_combustion(formula):
    import re
    match = re.match(r'C(\d*)H(\d*)', formula)
    if not match:
        return "Fórmula no válida. Debe seguir el formato CxHy, como C2H6."
    
    C_atoms = int(match.group(1)) if match.group(1) else 1
    H_atoms = int(match.group(2)) if match.group(2) else 1
    
    x, y, z = symbols('x y z')  # Coeficientes de O2, CO2 y H2O
    eq1 = Eq(C_atoms, y)  # Carbono balanceado
    eq2 = Eq(H_atoms, 2*z)  # Hidrógeno balanceado
    eq3 = Eq(2*x, 2*y + z)  # Oxígeno balanceado
    
    solution = solve((eq1, eq2, eq3), (x, y, z))
    
    O2_coeff = solution[x]
    CO2_coeff = solution[y]
    H2O_coeff = solution[z]
    
    return f"{formula} + {O2_coeff} O2 → {CO2_coeff} CO2 + {H2O_coeff} H2O"

if __name__ == "__main__":
    user_input = input("Ingrese la fórmula del hidrocarburo (ejemplo: C2H4): ")
    resultado = balance_combustion(user_input)
    print(resultado)
