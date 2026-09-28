import math
from typing import List


class Fraction:
    def __init__(self, numerator: int, denominator: int = 1):
        if denominator == 0:
            raise ValueError("на 0 нельзя делить")

        gcd_val = math.gcd(abs(numerator), abs(denominator))

        sign = -1 if (numerator * denominator) < 0 else 1

        self.num = sign * (abs(numerator) // gcd_val)
        self.den = abs(denominator) // gcd_val

    def __str__(self) -> str:
        if self.den == 1:
            return str(self.num)
        return f"{self.num}/{self.den}"

    def __repr__(self) -> str:
        return f"Fraction({self.num}, {self.den})"

    def __add__(self, other: "Fraction") -> "Fraction":
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other: "Fraction") -> "Fraction":
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other: "Fraction") -> "Fraction":
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other: "Fraction") -> "Fraction":
        return Fraction(self.num * other.den, self.den * other.num)


class Student:
    def __init__(self, name: str, age: int, grades: List[int]):
        self.name = name
        self.age = age
        self.grades = grades

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int)-> None:
        if value < 16 or value > 100:
            raise ValueError("Некорректный возраст студента (16-100)")
        self._age = value

    @property
    def gpa(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def __repr__(self) -> str:
        return f"Student(name='{self.name}', age={self.age}, gpa={self.gpa:.2f})"



f1 = Fraction(2, 4)
f2 = Fraction(3, 5)

print(f"Дробь 1: {f1}")
print(f"Дробь 2: {f2}")

print(f"{f1} + {f2} = {f1 + f2}")
print(f"{f1} - {f2} = {f1 - f2}")
print(f"{f1} * {f2} = {f1 * f2}")
print(f"{f1} / {f2} = {f1 / f2}")

students = [
        Student("Алексей", 19, [10, 10, 10, 10]),
        Student("Александр", 18, [3, 2, 2, 1]),
        Student("Дмитрий", 20, [4, 7, 8, 6]),
    ]
print("Список студентов:")
for s in students:
    print(f"{s.name}, Возраст: {s.age}, Средний балл: {s.gpa:.2f}")


sorted_students = sorted(students, key=lambda s: s.gpa, reverse=True)
print("Студенты отсортированные по среднему баллу:")
for s in sorted_students:
    print(f"{s.name}: {s.gpa:.2f}")