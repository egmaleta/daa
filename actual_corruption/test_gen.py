from random import randint, choices

from shared import FLOAT_INF as INF
from shared.testing import TestCase

from .sln_1_dikjstra import sln


class _TestGen:
    EMPTY = "empty"

    def __init__(self, n: int):
        assert n > 0
        self._n = n

    def __iter__(self):
        cases = []
        for _ in range(self._n):
            vertex_number = randint(2, 5)
            graph = [[INF for i in range(vertex_number)] for j in range(vertex_number)]

            for j in range(vertex_number):
                for k in range(vertex_number):
                    if j !=k:
                        r = choices([True, False])[0]
                        if r:
                            cost = randint(1, 10)
                            graph[j][k] = cost
                    else:
                        graph[j][k] = 0
            
            answer = sln(graph)
            yield TestCase(
                [graph],
                answer,
                lambda res: res == answer
            )

        return cases


TEST_GEN = _TestGen(10)
