import { open } from "node:fs/promises"

export function change(amount) {
  if (!Number.isInteger(amount)) {
    throw new TypeError("Amount must be an integer")
  }
  if (amount < 0) {
    throw new RangeError("Amount cannot be negative")
  }
  let [counts, remaining] = [{}, amount]
  for (const denomination of [25, 10, 5, 1]) {
    counts[denomination] = Math.floor(remaining / denomination)
    remaining %= denomination
  }
  return counts
}

// Write your first then lower case function here
export const firstThenLowerCase = (a, p) => {
  const solution = a.find(p)
  return solution?.toLowerCase()
}

// Write your powers generator here
// failing
export function* powersGenerator( {base, limit} ) {
  let exponent = 0
  while(base ** exponent <= limit) {
    yield base ** exponent
    exponent++
  }
}

// Write your say function here
export function say(word) {
  let words = []
  function chain(nextWord) {
    if (nextWord === undefined) {
      return words.join(' ')
    }
    words.push(nextWord)
    return chain
  }
  return chain(word)
}

// Write your line count function here
// only first test passing
export async function meaningfulLineCount(filePath) {
  let file;
  let meaningfulLines = 0;
  try {
    file = await open(filePath, 'r')
    const contents = await file.readFile('utf8')
    const lines = contents.split('\n')
    for (const line of lines) {
      const trimmed = line.trim();
      if (trimmed !== '' && !trimmed.startsWith('#')) {
        meaningfulLines++
      }
    }
  } catch (error) {
    throw error;
  } finally {
    if (file) await file.close();
  }
  return meaningfulLines
}

// Write your Quaternion class here
// failing, put it together quickly
export class Quaternion {
  constructor(a, b, c, d) {
    this.a = a
    this.b = b
    this.c = c
    this.d = d
    Object.freeze(this)
  }

  coefficients() {
    return [this.a, this.b, this.c, this.d]
  }

  conjugate() {
    return [this.a, this.b * -1, this.c * -1, this.d * -1]
  }

  plus (other) {
    return new Quaternion(
      this.a + other.a,
      this.b + other.b,
      this.c + other.c,
      this.d + other.d,
    )
  }

  times (other) {
    // complicated formula, did not have time
  }
};
