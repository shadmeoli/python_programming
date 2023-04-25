import click
from rich.console import Console
from functools import wraps


# info : this decorator helps increase performance
def memoize(func: callable) -> callable:

    # info : custom cache dictionary to hold computed vals
    CACHE = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in CACHE:
            CACHE[key] = func(*args, **kwargs)

        return CACHE[key]

    return wrapper


if __name__ == "__main__":
    console = Console()
    # ! functions
    @memoize
    def fib(n: int) -> int:

        if n < 2:
            return n
        return fib(n-1) + fib(n-1)

    val = int(click.prompt(" ++ Enter a fibonacci value to compute >>> ", default=50, show_default=True))
    console.print(f"[cyan bold]++ Counts : {fib(val)} [/cyan bold]")
    click.
        
