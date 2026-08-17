from math import gcd


class Fraction:
    """A fraction kept in simplified form."""

    def __init__(self, numerator, denominator):
        # Step 1
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

        common = gcd(numerator, denominator)

        self._numerator = numerator // common
        self._denominator = denominator // common

    def add(self, other):
        # Step 3
        n = (
            self._numerator * other._denominator
            + other._numerator * self._denominator
        )
        d = self._denominator * other._denominator

        return Fraction(n, d)

    def multiply(self, other):
        # Step 4
        n = self._numerator * other._numerator
        d = self._denominator * other._denominator

        return Fraction(n, d)

    def __str__(self):
        # Step 2
        return f"{self._numerator}/{self._denominator}"

    def __eq__(self, other):
        # Step 5
        if not isinstance(other, Fraction):
            return False

        return (
            self._numerator == other._numerator
            and self._denominator == other._denominator
        )


if __name__ == "__main__":
    # Run test_fraction.py for the full set of checks.
    print("Fraction starter file. Run: python test_fraction.py")