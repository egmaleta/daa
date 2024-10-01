from collections.abc import Callable

from shared.testing import TestCase, test


def sln(lb: int, ub: int, is_gt_M: Callable[[int], bool]):
    money = 1
    fuel = 0

    while ub - lb > 1:
        if money > 0:
            guess = (lb + ub) // 2
            if money < guess:
                guess = money
        else:
            guess = lb + 1
        
        fuel += 1
        
        if is_gt_M(guess):
            money -= guess
            ub = guess
        else:
            money += guess
            lb = guess
    
    return lb, fuel


class _TestGen:
    def __init__(self, M: int, max_fuel: int):
        assert M > 0
        assert 0 < max_fuel
        self._M = M
        self._max_fuel = max_fuel
    
    def __iter__(self):
        for i in range(self._M):
            yield TestCase(
                [0, self._M, lambda x: x > i],
                i,
                lambda res: res[0] == i and res[1] <= self._max_fuel
            )


test(sln, _TestGen(1015, 105))
