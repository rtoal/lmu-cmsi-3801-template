from dataclasses import dataclass
from collections.abc import Callable


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
def first_then_lower_case(a, p):
    '''
    
    '''
    for string in a:
        if p(string):
            return string.lower()
    return None

# Write your powers generator here
def powers_generator(base, limit):
    '''
    
    '''
    number = 0
    while base**number <= limit:
        yield base**number
        number += 1

# Write your say function here
def say(word=""):
    '''
    
    '''
    def next_word(next=None):
        if next is None:
            return next_word.word
        next_word.word += f" {next}"
        return next_word
    next_word.word = word
    return next_word

# Write your line count function here
def meaningful_line_count(file):
    '''
    Definition

    Parameters:

    Returns:

    Raises: 
    '''
    try:
        with open(file, "r", encoding="utf-8") as f:
            line_counter = 0
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                line_counter += 1
            return line_counter
    except FileNotFoundError:
        raise FileNotFoundError("No such file")\

# Write your Quaternion class here
class Quarternion():
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b + "i"
        self.c = c + "j"
        self.d = d + "k"
    
    def __str__(self):
        return
    

    def add():
        return 
    

    def multiply():
        return
    
    
    def coefficients():
        return
    
    def conjugate():
        return
