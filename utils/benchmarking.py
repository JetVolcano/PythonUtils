from collections.abc import Callable
from functools import wraps
from time import perf_counter
from itertools import repeat


def benchmark(func: Callable) -> Callable:
    """
    Decorator to benchmark a function
    :param func: "function to benchmark"
    when there is a TypeError when decorating your function please use the base function instead of the decorator
    :return: "docstring of parameter func"
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        results: list = []
        for _ in repeat(None, 50):
            start = perf_counter()
            func(*args, **kwargs)
            end = perf_counter()
            results.append(end - start)
        average: float = sum(results) / len(results)
        print(f"Benchmarking {func.__name__}({str(*args)+str(**kwargs)}) took {average:.8f} seconds")
    return wrapper