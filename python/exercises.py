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
# TODO: double check that this function uses positional arguments. seems like it is
def first_then_lower_case(strings: list[str], predicate: Callable[[str], bool]) -> Optional[str]:
  for idx in range(len(strings)):
    if strings[idx] != None and predicate(strings[idx]):
      return strings[idx].lower()
  return None

# Write your powers generator here
def powers_generator(base: int, limit: int):
    power: int = 1
    while power <= limit: 
        yield power
        power = power * base


# Write your say function here
def say(text: Optional[str] = None) -> Callable:
    ''' 
    Inner function chains the strings together to create final concatenated sentence. 
    '''
    sentence = []

    def final_sentence(next_text: Optional[str] = None) -> str:
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
def meaningful_line_count(path):
    try:
        f = open(path, "r")
    except:
        raise FileNotFoundError('No such file')
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
class Quaternion:
    a: int
    b: int
    c: int
    d: int

    @property 
    def __add__(q):
        return None

    @property
    def __multiply__(q):
        return None

    # def __eq__:
    #     return None
    
    # def __str__:
    #     return None
    

