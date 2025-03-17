from collections import deque
from collections.abc import Callable
from functools import wraps
from time import perf_counter
from itertools import repeat


def benchmark(func: Callable) -> Callable:
    """
    Decorator to benchmark a function
    ---
    when there is a TypeError when decorating your function please use the base function instead of the decorator like this:
    benchmark(func)(args)\n
    :param func: "function to benchmark"\n
    :type func: "Callable"\n
    :return: "docstring of parameter func"
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        results: deque[float | int] = deque()
        parameters: deque[tuple] = deque(*args+tuple(kwargs.items()), maxlen=1000)
        for _ in repeat(None, 15):
            start = perf_counter()
            ouput = func(*args, **kwargs)
            end = perf_counter()
            results.append(end - start)
        average: float = sum(results) / len(results)
        print(f"Benchmarking {func.__name__}{tuple(parameters)} took {average:.12f} seconds")
        return ouput
    return wrapper