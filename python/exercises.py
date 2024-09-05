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
def first_then_lower_case(strings: list[str], predicate: Callable[[str], bool]) -> Optional[str]:
  for idx in range(len(strings)):
    if strings[idx] != None and predicate(strings[idx]):
      return strings[idx].lower()
  return None



# Write your powers generator here


# Write your say function here


# Write your line count function here


# Write your Quaternion class here
