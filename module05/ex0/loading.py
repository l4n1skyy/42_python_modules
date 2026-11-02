import importlib
import importlib.metadata

REAGENTS: list[tuple] = [
    ("pandas", "Data manipulation ready"),
    ("numpy", "Numerical computation ready"),
]


def check_reagent(name: str, purpose: str) -> bool:
    try:
        importlib.import_module(name)
        version = importlib.metadata.version(name)
    except (ImportError, importlib.metadata.PackageNotFoundError):
        print(f"[MISSING] {name} - not installed")
        return False
    print(f"[OK] {name} ({version}) - {purpose}")
    return True


def print_install_help(missing: list[str]) -> None:
    print(f"\nMissing reagents: {', '.join(missing)}")
    print("Install them with either tool:")
    print("  pip:    pip install -r ex0/requirements.txt")
    print("  Poetry: poetry install")
    print("          poetry run python ex0/loading.py")


def print_pip_vs_poetry() -> None:
    print("\npip vs Poetry:")
    print(
        "  requirements.txt declares what to install; pip resolves it at install time."
    )
    print("  pyproject.toml declares the same constraints, and Poetry pins")
    print("  the resolved versions in poetry.lock so every install is identical.")


def main() -> None:
    print("\nREAGENT STATUS: Loading reagents...\n")
    print("Checking dependencies:")
    missing: list[str] = []
    for name, purpose in REAGENTS:
        if not check_reagent(name, purpose):
            missing.append(name)
    if missing:
        print_install_help(missing)
    print_pip_vs_poetry()
    if not missing:
        print("\nAll reagents present and accounted for.")


if __name__ == "__main__":
    main()
