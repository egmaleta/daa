from os import listdir
from pathlib import Path
from random import randint

from shared.testing import TestCase

from .grafo import Grafo
from .sln_1_bt import sln as bruteforce


TESTS_FILE = "corruption_testcases.txt"


class _TestGen:
    EMPTY = "empty"

    def __init__(self, n: int):
        assert n > 0
        self._n = n

    def _encode(self, k, streets, lengths):
        if len(streets) == 0:
            streets = self.EMPTY
        else:
            streets = ",,".join(",".join(str(x) for x in t) for t in streets)
        
        if len(lengths) == 0:
            lengths = self.EMPTY
        else:
            lengths = ",,".join(",".join(str(x) for x in t) for t in lengths)
        
        return ",,,".join([str(k), streets, lengths])
    
    def _decode(self, s: str):
        k, streets, lengths = s.split(",,,")

        k = int(k)

        if streets == self.EMPTY:
            streets = []
        else:
            streets = [tuple(int(x) for x in chunk.split(",")) for chunk in streets.split(",,")]
        
        if lengths == self.EMPTY:
            lengths = set()
        else:
            lengths = {tuple(int(x) for x in chunk.split(",")) for chunk in lengths.split(",,")}
        
        return k, streets, lengths
    
    def _gen_tc(self):
        k = randint(5, 10)

        max_edges = k * (k - 1) // 2
        edges = randint(1, max_edges)

        streets = {}
        for _ in range(edges):
            v = randint(0, k - 1)
            w = randint(0, k - 1)
            if v == w:
                continue

            streets[(v, w)] = randint(1, 10)
        
        streets = [(v, w, weight) for (v, w), weight in streets.items()]

        g = Grafo()
        for v, w, weight in streets:
            g.agregar_arista(v, w, weight)
        
        lengths = set(bruteforce(g))

        return k, streets, lengths


    def __iter__(self):
        file_path = Path.cwd() / TESTS_FILE

        if TESTS_FILE not in listdir(Path.cwd()):
            tests = [self._gen_tc() for _ in range(self._n)]
            with open(file_path, "x") as file:
                file.write("\n".join(
                    self._encode(k, ss, ls) for k, ss, ls in tests
                ))
        else:
            tests = []
            with open(file_path) as file:
                tests = [self._decode(s) for s in file.read().split("\n")]
        
        for k, streets, lengths in tests:
            lengths = lengths
            yield TestCase(
                [k, streets],
                lengths,
                lambda res: res == lengths
            )


TEST_GEN = _TestGen(100)
