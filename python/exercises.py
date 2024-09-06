from dataclasses import dataclass
from collections.abc import Callable
import os

def change(amount: int) -> dict[int, int]:
    if not isinstance(amount, int):
        raise TypeError('Amount must be an integer')
    if amount < 0:
        raise ValueError('Amount cannot be negative')
    counts, remaining = {}, amount
    for denomination in (25, 10, 5, 1):
        counts[denomination], remaining = divmod(remaining, denomination)
    return counts


# Write your first then lower case function here
def first_then_lower_case(strings: list[str], predicate: Callable[[str], bool]) -> str | None:
    if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
        raise TypeError('First argument must be a list of strings')
    
    if not callable(predicate):
        raise TypeError('Second argument must be a callable predicate function')
    
    filtered = [s for s in strings if predicate(s)]
    
    if not filtered:
        return None
    first_valid_string = filtered[0]
    return first_valid_string.lower()


# Write your powers generator here
def powers_generator(base: int, limit: int):
    exponent = 0
    while True:
        result = base ** exponent
        if result > limit:
            break
        yield result
        exponent += 1

# Write your say function here
class Say:
    def __init__(self, *args):
        self.phrase = " ".join(args)
    
    def __call__(self, *args):
        if not args:
            return self.phrase
        new_phrase = self.phrase + " " + " ".join(args)
        return Say(new_phrase)

def say(*args):
    if not args: 
        return ""
    return Say(*args)

# Write your line count function here
def meaningful_line_count(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError('No such file')
    
    meaningful_line_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                meaningful_line_count += 1
    return meaningful_line_count

# Write your Quaternion class here
class Quaternion:
    def __init__(self, a=0.0, b=0.0, c=0.0, d=0.0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    @property
    def coefficients(self):
        return (self.a, self.b, self.c, self.d)

    @property
    def conjugate(self):
        return Quaternion(self.a, -self.b, -self.c, -self.d)

    def __add__(self, other):
        return Quaternion(
            self.a + other.a,
            self.b + other.b,
            self.c + other.c,
            self.d + other.d
        )

    def __mul__(self, other):
        a1, b1, c1, d1 = self.a, self.b, self.c, self.d
        a2, b2, c2, d2 = other.a, other.b, other.c, other.d
        return Quaternion(
            a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2,
            a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
            a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2,
            a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2
        )

    def __eq__(self, other):
        return (self.a, self.b, self.c, self.d) == (other.a, other.b, other.c, other.d)

    def __repr__(self):
        parts = []
        if self.a != 0:
            parts.append(f"{self.a}")
        for coeff, symbol in [(self.b, 'i'), (self.c, 'j'), (self.d, 'k')]:
            if coeff != 0:
                if abs(coeff) == 1:
                    part = f"{'-' if coeff < 0 else ''}{symbol}"
                else:
                    part = f"{coeff}{symbol}"
                parts.append(part)
        if not parts:
            return '0'
        result = parts[0]
        for part in parts[1:]:
            if part.startswith('-'):
                result += part
            else:
                result += '+' + part
        return result
