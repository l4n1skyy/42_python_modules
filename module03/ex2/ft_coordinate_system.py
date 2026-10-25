import math


def get_player_pos() -> tuple[float, ...]:
    while True:
        input_str = input(
            "Enter new coordinates as floats in format 'x,y,z': ",
        )
        input_lst = input_str.split(",")
        float_lst: list[float] = []
        try:
            _, _, _ = input_lst
        except ValueError:
            print("Invalid syntax")
            continue

        for i in input_lst:
            try:
                float_lst += [float(i)]

            except ValueError as e:
                print(f"Error on parameter '{i}': {e}")
                break
        else:
            return (*float_lst,)


def dis_bw_coords(c1: tuple[float, ...], c2: tuple[float, ...]) -> float:
    x1, y1, z1 = c1
    x2, y2, z2 = c2

    m_add = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
    m_sqrt = math.sqrt(m_add)
    m_round = round(m_sqrt, 4)

    return m_round


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("\nGet a first set of coordinates")
    first_coords = get_player_pos()
    x, y, z = first_coords
    print(f"Got a first tuple: {first_coords}")
    print(f"It includes: X={x}, Y={y}, Z={z}")
    dis_to_cent = dis_bw_coords((0.0, 0.0, 0.0), first_coords)
    print(f"Distance to center: {dis_to_cent}")

    print("\nGet a second set of coordinates")
    second_coords = get_player_pos()
    print(
        "Distance between the 2 sets of coordinates:",
        f"{dis_bw_coords(first_coords, second_coords)}",
    )
