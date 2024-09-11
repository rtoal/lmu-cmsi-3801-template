from dataclasses import dataclass
from collections.abc import Callable
from typing import Optional
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
def first_then_lower_case(strings: list[str], predicate: Callable[[str], bool]) -> Optional[str]:
  for idx in range(len(strings)):
    if strings[idx] != None and predicate(strings[idx]):
      return strings[idx].lower()
  return None

# Write your powers generator here
def powers_generator(*, base: int, limit: int):
    power: int = 1
    while power <= limit:
        yield power
        power = power * base

# Write your say function here
def say(text: Optional[str] = None) -> Callable | str:
    ''' 
    Inner function chains the strings together to create final concatenated sentence. 

    String concatenation guide to use .join method: https://www.digitalocean.com/community/tutorials/python-string-concatenation
    '''
    sentence: list[str] = []

    def final_sentence(next_text: Optional[str] = None) -> str | Callable:
        if next_text is None:
            return " ".join(sentence)
        else:
            sentence.append(next_text)

        return final_sentence
    
    if text is None:
        return ""
    
    sentence.append(text)

    return final_sentence

# Write your line count function here
def meaningful_line_count(path: str) -> int:
    path = os.path.join(os.path.dirname(__file__), "..", path)

    try:
        f = open(path, "r")
    except:
        raise FileNotFoundError("No such file")
    count = 0
    for line in f.readlines():
        newLine = line.strip()
        if len(newLine) == 0 or newLine[0] == "#":
            continue
        count += 1
    f.close()
    return count

# Write your Quaternion class here
@dataclass (frozen = True)
class Quaternion():
    a: int
    b: int
    c: int
    d: int

    def __add__(self, q):
        return Quaternion(self.a + q.a, self.b + q.b, self.c + q.c, self.d + q.d)
    
    def __mul__(self, q):
        return Quaternion(((self.a * q.a) - (self.b * q.b) - (self.c * q.c) - (self.d * q.d)),
                          ((self.a * q.b) + (self.b * q.a) + (self.c * q.d) - (self.d * q.c)),
                          ((self.a * q.c) - (self.b * q.d) + (self.c * q.a) + (self.d * q.b)),
                          ((self.a * q.d) + (self.b * q.c) - (self.c * q.b) + (self.d * q.a)))
    
    @property 
    def coefficients(self):
        return (self.a, self.b, self.c, self.d)

    @property
    def conjugate(self):
        return Quaternion(self.a, (-1 * self.b), (-1 * self.c), (-1 * self.d))

    def __eq__(self, q):
        return self.a == q.a and self.b == q.b and self.c == q.c and self.d == q.d
    
    def __str__(self):
        output = ""

        if self.a != 0:
            output += f'{self.a}'

        if self.b != 0:
            if self.b == 1:
                if output == "":
                    output += "i"
                else:
                    output += "+i"
            elif self.b > 1:
                output += "+" + f'{self.b}i'
            elif self.b == -1:
                output += "-i"
            else:
                output += f'{self.b}i'

        if self.c != 0:
            if self.c == 1:
                if output == "":
                    output += "j"
                else:
                    output += "+j"
            elif self.c > 1:
                output += "+" + f'{self.c}j'
            elif self.c == -1:
                output += "-j"
            else:
                output += f'{self.c}j'
                
        if self.d != 0:
            if self.d == 1:
                if output == "":
                    output += "k"
                else:
                    output += "+k"
            elif self.d > 1:
                output += "+" + f'{self.d}k'
            elif self.d == -1:
                output += "-k"
            else:
                output += f'{self.d}k'

        return output or "0"