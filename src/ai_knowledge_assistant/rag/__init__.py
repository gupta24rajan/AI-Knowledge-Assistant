import runpy
from pathlib import Path


def main() -> None:
    module_path = Path(__file__).parent / "main.py"
    runpy.run_path(str(module_path), run_name="__main__")