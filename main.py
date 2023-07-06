from sys import argv
from src.runner import Runner


filename: str = argv[-1]

with open(filename, "r", encoding="utf-8") as f:
    script: str = f.read()


lines: list = script.split("\n")


runner: Runner = Runner(lines, filename)
runner.run()