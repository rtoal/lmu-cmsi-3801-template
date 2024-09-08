import { open } from "node:fs/promises"
import { readFile } from "node:fs/promises"

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
export function firstThenLowerCase(strings, predicate) {
  for (let idx = 0; idx < strings?.length; idx++) {
    if (strings[idx]?.toLowerCase() && predicate(strings[idx])) {
      return strings?.[idx].toLowerCase()
    }
  }
  return undefined
}

// Write your powers generator here
export function* powersGenerator({ofBase: base, upTo: limit}) {
  let power = 1
  while (power <= limit) {
      yield power
      power = base * power
  }
}

// Write your say function here
export function say(text = undefined) {
  /*
  Chains multiple function calls and adding each word into an array, returning a sentence/phrase.
  */
  const sentence = []

  function final_sentence(next_text = undefined) {
    if (next_text === undefined) {
      return sentence.join(" ")
    } else {
      sentence.push(next_text)
    }
    return final_sentence
  }
  if (text === undefined) {
    return ""
  }

  sentence.push(text)

  return final_sentence
}
// Write your line count function here
export async function meaningfulLineCount(path) {
  // Aspects inspired by https://www.geeksforgeeks.org/node-js-filehandle-readlines-method/
  console.log("testing")
  const file = await open(path)
    let count = 0
  const fileString = await readFile(path, { encoding: "utf8"})
  fileString.split("\n").forEach(line => {
    line = line.trim()
    if (!(line.length == 0 || line[0] == "#")) {
      count += 1
    }
  });
  return count
}

// Write your Quaternion class here
