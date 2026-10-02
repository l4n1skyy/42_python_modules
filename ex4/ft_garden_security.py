def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    rose = Plant("rose", 15.0, 10)
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    rose.set_age(-5)
    print("Current state: ", end="")
    rose.show()


class Plant:
    # Constructor
    def __init__(
        self,
        name: str = "Unknown",
        height: float = 1.0,
        age: int = 1,
        rate: float = 1.0,
    ) -> None:
        self._name = name.capitalize()

        if height < 0.0:
            print(f"{self._name}: Error, height can't be negative")
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
        if rate < 0.0:
            print(f"{self._name}: Error, rate can't be negative")

        self._height = height + 0.0 if height >= 0 else 1.0
        self._age = age if age >= 0 else 1
        self._rate = rate if rate >= 0.0 else 1.0
        print("Plant created: ", end="")
        self.show()

    # Methods
    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def grow(self, days: int) -> float:
        self._height = round(self._height + days * self._rate, 1)
        return self._height

    def age(self, days: int) -> int:
        self._age += days
        return self._age

    # Getters
    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_rate(self) -> float:
        return self._rate

    def get_name(self) -> str:
        return self._name

    # Setters
    def set_height(self, height: float) -> None:
        if height >= 0.0:
            self._height = height + 0.0
            print(f"Height updated: {height}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
            print(f"Age updated: {age} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def set_rate(self, rate: float) -> None:
        if rate >= 0.0:
            self._rate = rate
        else:
            print(f"{self._name}: Error, rate can't be negative")
            print("Rate update rejected")

    def set_name(self, name: str) -> None:
        if name != "" and name != " ":
            self._name = name.capitalize()
        else:
            print(f"{self._name}: Error, name can't be empty")
            print("Name update rejected")


if __name__ == "__main__":
    ft_garden_security()
