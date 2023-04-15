from rich.console import Console

console = Console()


def target_calc(
        target: float = 20000.50,
        savings_per_duration: int = 5000) -> list[int]:
    # see all savings iterations
    total_saved: list[int] = []
    while sum(total_saved) < target:
        # calculate savings
        total_saved.append(savings_per_duration)

    return total_saved


offset = round(((sum(target_calc()) - 20000) * 100) / 20000, 1)

if __name__ == "__main__":
    console.print(
        f" [magenta]>>>[/magenta] Saving duration : [green bold]{len(target_calc() * 7)} days[/green bold];\n [magenta]>>>[/magenta] Total saved : [blue bold]KES.{sum(target_calc())}[/blue bold]\n [magenta]>>>[/magenta] Target offset at: [cyan bold]{offset}%[/cyan bold]")
    console.print(f" [magenta]>>>[/magenta] [blue bold]KES.{sum(target_calc())}[/blue bold]")
