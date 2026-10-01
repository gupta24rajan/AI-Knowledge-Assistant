from pathlib import Path


def find_project_root():
    current = Path(__file__).resolve()

    for parent in current.parents:
        if (parent / "pyproject.toml").exists():
            return parent

    raise RuntimeError("Could not find project root")


PROJECT_ROOT = find_project_root()


def resolve_path(file_path):
    path = Path(file_path)

    if path.is_absolute():
        return path

    return PROJECT_ROOT / path