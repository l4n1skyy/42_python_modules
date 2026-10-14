def test_temperature() -> None:
    tests = ["25", "abc", "100", "-50"]
    print("=== Garden Temperature ===")
    for t in tests:
        print(f"Input data is '{t}'")
        try:
            temp = input_temperature(t)
            print(f"Temperature is now {temp}°C")
        except (ValueError, TypeError) as e:
            print(f"Caught input_temperature error: {e}")
    print("All tests completed - program didn't crash!")


def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0 or temp > 40:
        raise ValueError(f"{temp}°C is out of range (must be 0 to 40°C)")
    return temp


if __name__ == "__main__":
    test_temperature()
