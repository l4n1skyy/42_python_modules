def ft_count_harvest_iterative():
    n = int(input("Days until harvest: "))
    i = 0
    while (i := i + 1) < n + 1:
        print(f"Day {i}")
    print("Harvest time!")


# walrus operator
# while (n := n - 1) > 0:
# n-- equivalent
#
# * unpacking operator
# print(*range(4), sep="\n") becomes print(0, 1, 2, 3, sep="\n")
