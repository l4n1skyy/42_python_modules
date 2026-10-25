import sys
import typing


def f_update() -> None:

    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
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
        sys.stderr.write(f"[STDERR] Error reading file '{fname}': {e}\n")
        return
    finally:
        f.close()
        print(f"File '{fname}' closed.")

    print(f"\nTransform data:\n---\n\n{new_content}\n---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    fname = sys.stdin.readline().strip()
    if fname == "":
        print("Not saving data.")
        return
    f = f_validate(fname, "w")
    if not f:
        print("Data not saved.")
        return
    try:
        f.write(new_content)
    except (OSError, ValueError) as e:
        sys.stderr.write(f"[STDERR] Error writing file '{fname}': {e}\n")
        print("Data not saved.")
        return
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
        sys.stderr.write(f"[STDERR] Error opening file '{fname}': {e}\n")
        return None
    else:
        return f


if __name__ == "__main__":
    f_update()
