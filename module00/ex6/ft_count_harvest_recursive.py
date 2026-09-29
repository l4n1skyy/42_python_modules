def ft_count_harvest_recursive(n=None):
    if n is None:
        n = int(input("Days until harvest: "))
        ft_count_harvest_recursive(n)
        print("Harvest time!")
        return
    if n == 0:
        return
    ft_count_harvest_recursive(n - 1)
    print(f"Day {n}")
