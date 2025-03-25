import pathlib
import subprocess

from rich.console import Console

from cyoag.theme import theme_1

rich = Console(theme=theme_1)

project_root = pathlib.Path(__file__).resolve().parents[2]
src_dir = project_root / "source" / "cyoag"


def tidy():
    rich.print("\n[b bright_white]Tidying up project...[/]")
    rich.print("\n[b bright_white]Black:[/]")
    subprocess.run(["black", str(src_dir)], check=True)

    rich.print("\n[b bright_white]isort:[/]")
    subprocess.run(["isort", str(src_dir)], check=True)

    rich.print("\n[b bright_white]Ruff:[/]")
    subprocess.run(["ruff", "check", "--fix", str(src_dir)], check=True)


def tidy_check():
    rich.print("\n[b bright_white]Checking project...[/]")
    rich.print("\n[b bright_white]Black:[/]")
    subprocess.run(["black", "--diff", "--color", str(src_dir)], check=True)

    rich.print("\n[b bright_white]isort:[/]")
    subprocess.run(["isort", "--check", "--diff", str(src_dir)], check=True)

    rich.print("\n[b bright_white]Ruff:[/]")
    subprocess.run(["ruff", "check", str(src_dir)], check=True)


def tidy_verbose():
    rich.print("\n[b bright_white]Checking project (verbose)...[/]")
    rich.print("\n[b bright_white]Black:[/]")
    subprocess.run(
        ["black", "-v", "--diff", "--color", str(src_dir)], check=True
    )

    rich.print("\n[b bright_white]isort:[/]")
    subprocess.run(
        ["isort", "-v", "--check", "--diff", str(src_dir)], check=True
    )

    rich.print("\n[b bright_white]Ruff:[/]")
    subprocess.run(["ruff", "check", "-v", str(src_dir)], check=True)
