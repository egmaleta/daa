from typing import Callable, Tuple

def sln_backtrack(lb: int, ub: int, is_gt_M: Callable[[int], bool]) -> Tuple[int, int]:
    def backtrack(current_lb: int, current_ub: int, money: int, fuel: int) -> Tuple[int, int]:
        # Caso base: si el rango se reduce a un solo elemento
        if current_ub - current_lb <= 1:
            return current_lb, fuel
        
        if money > 0:
            guess = (current_lb + current_ub) // 2
            if money < guess:
                guess = money
        else:
            guess = current_lb + 1
        
        fuel += 1
        
        if is_gt_M(guess):
            return backtrack(current_lb, guess, money - guess, fuel)
        else:
            return backtrack(guess, current_ub, money + guess, fuel)

    initial_money = 1
    initial_fuel = 0
    
    return backtrack(lb, ub, initial_money, initial_fuel)

# Ex
def is_gt_M(guess: int) -> bool:
    M = 876  # Valor de comparación
    return guess > M

result = sln_backtrack(1, 10**14, is_gt_M)
print(result)  