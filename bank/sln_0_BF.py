from typing import Callable, Tuple

def sln_brute_force(lb: int, ub: int, is_gt_M: Callable[[int], bool]) -> Tuple[int, int]:
    money = 1
    fuel = 0

    # Iterar desde el límite inferior hasta el límite superior
    for guess in range(lb + 1, ub):  # Comenzamos desde lb + 1 hasta ub - 1
        fuel += 1  # Incrementar el combustible por cada intento

        if is_gt_M(guess):
            return guess-1, fuel
            # money -= guess  # Reducir el dinero si la adivinanza es mayor
            # # Si se queda sin dinero, no se puede seguir
            # if money < 0:
            #     break
        # else:
        #     money += guess  # Aumentar el dinero si la adivinanza no es mayor
    return None    

        

# Ejemplo de uso
def is_gt_M(guess: int) -> bool:
    M = 10 # Valor de comparación
    return guess > M

# Llamada a la función
result = sln_brute_force(1, 1014, is_gt_M)
print(result)  # Output esperado: (valor final de lb, cantidad de fuel)