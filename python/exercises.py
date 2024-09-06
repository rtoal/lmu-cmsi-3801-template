from dataclasses import dataclass
from collections.abc import Callable
from typing import Optional


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


# Write your powers generator here


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


# Write your Quaternion class here
