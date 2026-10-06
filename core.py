"""App logic, kept free of Kivy imports so it can be unit-tested anywhere."""


class Counter:
    """A simple counter with optional bounds."""

    def __init__(self, start: int = 0, minimum: int | None = None, maximum: int | None = None):
        self.minimum = minimum
        self.maximum = maximum
        self.value = start

    def increment(self, step: int = 1) -> int:
        self.value += step
        if self.maximum is not None:
            self.value = min(self.value, self.maximum)
        return self.value

    def decrement(self, step: int = 1) -> int:
        self.value -= step
        if self.minimum is not None:
            self.value = max(self.value, self.minimum)
        return self.value

    def reset(self) -> int:
        self.value = 0
        return self.value
