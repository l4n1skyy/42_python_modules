def secure_archive(
    fname: str,
    mode: str = "r",
    content: str = "",
) -> tuple[bool, str]:
    try:
        if mode not in ["r", "w"]:
            return (False, f"Unsupported action: '{mode}'")
        with open(fname, mode) as f:
            if mode == "r":
                return (True, f.read())
            else:
                f.write(content)
                return (True, "Content successfully written to file")
    except (OSError, ValueError) as e:
        return (False, str(e))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    ok, text = secure_archive("ancient_fragment.txt")
    print((ok, text))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_fragment.txt", "w", text))
