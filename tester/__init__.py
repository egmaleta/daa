from collections.abc import Generator, Callable
from typing import Any, NamedTuple, Protocol


class TestCase[T](NamedTuple):
    args: list[Any]
    expected_result: T


class ITestGen[T](Protocol):
    def __iter__(self) -> Generator[TestCase[T]]:
        pass


def test[T](impl: Callable[..., T], test_gen: ITestGen[T] | Generator[TestCase[T]]):
    for n, (args, expected) in enumerate(test_gen, start=1):
        result = impl(*args)
        assert result == expected, f"Test #{n} with args '{args}' failed: got '{result}', expected '{expected}'."
