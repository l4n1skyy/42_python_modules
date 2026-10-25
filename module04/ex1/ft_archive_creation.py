import sys
import typing


def f_update() -> None:

    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")

    fname = sys.argv[1]
    f = f_validate(fname, "r")
    new_content = ""
    if not f:
        return

    try:
        old_content = f.read()
        print(f"---\n\n{old_content}\n---")

        for line in old_content.splitlines():
            new_line = f"{line}#\n"
            new_content += new_line

    except (OSError, ValueError) as e:
        print(f"Error reading file '{fname}': {e}")
        return
    finally:
        f.close()
        print(f"File '{fname}' closed.")

    print(f"\nTransform data:\n---\n\n{new_content}\n---")

    fname = input("Enter new file name (or empty): ")
    if fname == "":
        print("Not saving data.")
        return
    f = f_validate(fname, "w")
    if not f:
        return
    try:
        f.write(new_content)
    except (OSError, ValueError) as e:
        print(f"Error writing file '{fname}': {e}")
        return None
    finally:
        f.close()
    print(f"Data saved in file '{fname}'.")


def f_validate(fname: str, mode: str) -> typing.IO | None:
    try:
        if mode == "r":
            print(f"Accessing file '{fname}'")
        if mode == "w":
            print(f"Saving data to '{fname}'")
        f = open(fname, mode)
    except OSError as e:
        print(f"Error opening file '{fname}': {e}")
        return None
    else:
        return f


if __name__ == "__main__":
    f_update()
