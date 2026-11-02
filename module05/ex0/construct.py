import sys
import site
import os


def in_venv() -> bool:
    return sys.prefix != sys.base_prefix


def get_python() -> str:
    return sys.executable


def get_venv() -> str:
    #   return sys.prefix.rsplit("/", maxsplit=1)[1]
    return os.path.basename(sys.prefix)


def get_env() -> str:
    return sys.prefix


def get_site_packages() -> list[str]:
    return site.getsitepackages()


def print_sealed() -> None:
    print("\nLABORATORY STATUS: The laboratory is sealed\n")
    print(f"Current Python: {get_python()}")
    print(f"Virtual Environment: {get_venv()}")
    print(f"Environment Path: {get_env()}\n")
    print("SUCCESS: You are working in an isolated environment!")
    print("Safe to install reagents without affecting")
    print("the global system.\n")
    print("Reagent installation path:")
    for path in get_site_packages():
        print(path)


def print_open() -> None:
    print("\nLABORATORY STATUS: You are working in the open\n")
    print(f"Current Python: {get_python()}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You are in the global environment!")
    print("Every reagent you install here leaks into the whole system.\n")
    print("To seal the laboratory, run:")
    print("python3 -m venv lab_env")
    print("source lab_env/bin/activate # On Unix")
    print("lab_env\\Scripts\\activate # On Windows\n")
    print("Then run this program again.")


if __name__ == "__main__":
    if in_venv():
        print_sealed()
    else:
        print_open()
