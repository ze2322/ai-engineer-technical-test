from pathlib import Path

def create_directory(path: Path):
    path.mkdir(parents=True, exist_ok=True)