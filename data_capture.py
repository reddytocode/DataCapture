class Number:
    """
    Describes each number and its own stats
    """

    def __init__(self, value: int, count: int = 1, less: int = 0, greater: int = 0) -> None:
        self.value: int = value

        self.less: int = less
        self.count: int = count
        self.greater: int = greater

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Number):
            return False

        fields = ["value", "less", "count", "greater"]
        return any([getattr(self, field) == getattr(other, field) for field in fields])


class Stats:
    def __init__(self, stats: dict[int, Number]) -> None:
        self.data: dict[int, Number] = stats

    def less(self, value: int) -> int:
        return self.data[value].less

    def greater(self, value: int) -> int:
        return self.data[value].greater

    def between(self, a: int, b: int) -> int:
        return self.less(max(a, b)) - self.less(min(a, b)) + 1


class DataCapture:
    def __init__(self) -> None:
        self.numbers: dict[int, Number] = {}
        self.count: int = 0

    def add(self, value: int) -> None:
        if not isinstance(value, int) or not (0 <= value < 1000):
            raise ValueError(f"Invalid value ({value})")

        self.count += 1

        if value in self.numbers:
            self.numbers[value].count += 1
            return

        self.numbers[value] = Number(value)

    def build_stats(self) -> Stats:
        less: int = 0
        greater: int = self.count

        # O(n lon(n)) + O(n) -> O(n log(n))
        for key in sorted(self.numbers.keys()):
            number: Number = self.numbers[key]

            count: int = number.count
            greater -= count

            number.less = less
            number.greater = greater

            less += count

        return Stats(self.numbers)
