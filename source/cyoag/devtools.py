import subprocess


def tidy():
    subprocess.run(["black", "source/"], check=True)
    subprocess.run(["isort", "source/"], check=True)
    subprocess.run(["ruff", "check", "source/"], check=True)
