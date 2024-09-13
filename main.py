from tester import TestCase, test


class FooTester:
    def __init__(self, n: int):
        assert n > 0
        self._n = n
    
    def __iter__(self):
        for x in range(self._n):
            yield TestCase([x], x)


def identity(x):
    return x


if __name__ == "__main__":
    tester = FooTester(100)
    test(identity, tester)
