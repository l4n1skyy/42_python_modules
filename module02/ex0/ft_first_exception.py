def test_temperature() -> None:
    tests = ["25", "abc"]
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
    return int(temp_str)


if __name__ == "__main__":
    test_temperature()
