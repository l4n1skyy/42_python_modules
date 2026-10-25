import sys


def f_validate() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    try:
        print(f"Accessing file '{sys.argv[1]}'")
        f = open(sys.argv[1], "r")
    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
        return

    try:
        print(f"---\n\n{f.read()}\n---")
    except (OSError, ValueError) as e:
        print(f"Error reading file '{sys.argv[1]}': {e}")
    finally:
        f.close()
        print(f"File '{sys.argv[1]}' closed.")


if __name__ == "__main__":
    f_validate()
