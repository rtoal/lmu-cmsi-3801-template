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
        raise FileNotFoundError("No such file")

# Write your Quaternion class here
class Quaternion():
    def __init__(self, a, b, c, d):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)
    
    def __eq__(self, other):
        if isinstance(other, Quaternion):
            if self.a == other.a:
                pass
            else:
                return False
            if self.b == other.b:
                pass
            else:
                return False
            if self.c == other.c:
                pass
            else:
                return False
            if self.d == other.d:
                pass
            else:
                return False
            return True
    
    def __str__(self):
        local_a = str(self.a)
        local_b = str(self.b)
        local_c = str(self.c)
        local_d = str(self.d)
        if local_a == "0.0":
            local_a = ""
        if local_b == "0.0" or local_b == "-0.0":
            local_b = ""
        if local_c == "0.0" or local_c == "-0.0":
            local_c = ""
        if local_d == "0.0" or local_d == "-0.0":
            local_d = ""

        if local_b != "":
            if local_b == "1.0" or local_b == "-1.0":
                if local_b == "-1.0":
                    local_b = "-"
                else:
                    local_b = ""
            local_b = local_b + "i"
        if local_c != "":
            if local_c == "1.0" or local_c == "-1.0":
                if local_c == "-1.0":
                    local_c = "-"
                else:
                    local_c = ""
            local_c = local_c + "j"
        if local_d != "":
            if local_d == "1.0" or local_d == "-1.0":
                if local_d == "-1.0":
                    local_d = "-"
                else:
                    local_d = ""
            local_d = local_d + "k"
        
        # needs to check if b is "", if that is, then check c, if that is then check d. if all are "" then pass.

        if local_b == "":
            if local_c == "":
                if local_d == "":
                    pass
                else:
                    if local_d[0] != "-" and local_a != "":
                        local_a = local_a + "+"
            else:
                if local_c[0] != "-" and local_a != "":
                    local_a = local_a + "+"
        else:
            if local_b[0] != "-" and local_a != "":
                local_a = local_a + "+"

        # if local_b == "" and local_c == "" and local_d == "":
        #     pass
        # else:
        #     if local_b[0] != "-" and local_a != "":
        #         local_a = local_a + "+"
        if local_c == "":
            if local_d == "":
                pass
            else:
                if local_d[0] != "-" and local_a != "":
                    local_a = local_a + "+"
        else:
            if local_c[0] != "-" and local_a != "":
                local_a = local_a + "+"
        if local_d == "":
            pass
        else:
            if local_d[0] != "-" and local_c != "":
                local_c += "+"
        
        print(local_a + local_b + local_c + local_d)

        return local_a + local_b + local_c + local_d

    def __add__(self, other):
        if isinstance(other, Quaternion):
            new_a = self.a + other.a
            new_b = self.b + other.b
            new_c = self.c + other.c
            new_d = self.d + other.d
            return Quaternion(new_a, new_b, new_c, new_d)

    def __mul__(self, other):
        if isinstance(other, Quaternion):
            new_a = (self.a * other.a) - (self.b * other.b) - (self.c * other.c) - (self.d * other.d)
            new_b = (self.a * other.b) + (self.b * other.a) + (self.c * other.d) - (self.d * other.c)
            new_c = (self.a * other.c) - (self.b * other.d) + (self.c * other.a) + (self.d * other.b)
            new_d = (self.a * other.d) + (self.b * other.c) - (self.c * other.b) + (self.d * other.a)
            return Quaternion(new_a, new_b, new_c, new_d)
    
    @property
    def coefficients(self):
        return self.a, self.b, self.c, self.d
    
    @property
    def conjugate(self):
        return Quaternion(self.a, self.b * -1, self.c * -1, self.d * -1)
