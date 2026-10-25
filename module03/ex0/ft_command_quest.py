import sys


def ft_command_quest():
    argc = len(sys.argv)
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    try:
        if argc <= 1:
            raise Exception("No arguments provided!")
        print(f"Arguments received: {argc - 1}")
        for i in range(1, argc):
            print(f"Argument {i}: {sys.argv[i]}")
    except Exception as e:
        print(e)
    finally:
        print(f"Total arguments: {argc}")


if __name__ == "__main__":
    ft_command_quest()
