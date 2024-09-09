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
export class Quaternion {
  constructor(a, b ,c ,d) {
    this.a = a;
    this.b = b;
    this.c = c;
    this.d = d;
    Object.freeze(this);
  }
  plus(q) {
    return new Quaternion(this.a + q.a, this.b + q.b, this.c + q.c, this.d + q.d);
  }

  times(q) {
    return new Quaternion(((this.a * q.a) - (this.b * q.b) - (this.c * q.c) - (this.d * q.d)),
                          ((this.a * q.b) + (this.b * q.a) + (this.c * q.d) - (this.d * q.c)),
                          ((this.a * q.c) - (this.b * q.d) + (this.c * q.a) + (this.d * q.b)),
                          ((this.a * q.d) + (this.b * q.c) - (this.c * q.b) + (this.d * q.a)));
  }

  get coefficients() {
    return [this.a, this.b, this.c, this.d];
  }
  get conjugate() {
    return new Quaternion(this.a, (-1 * this.b), (-1 * this.c), (-1 * this.d))
  }

  equals(q) {
    return this.a === q.a, this.b === q.b, this.c === q.c, this.d === q.d
  }

  toString() {
    let output = "";

    if (this.a !== 0) { 
      output += `${this.a}` 
    };

    if (this.b !== 0) { 
      if (this.b === 1) { 
        if (output === "") { output += "i" } else { output += "+i"}
      } else if (this.b > 1) { 
        output += "+" + `${this.b}i` 
      } else if (this.b === -1) { 
        output += "-i" 
      } else { output += `${this.b}i` }
    };

    if (this.c !== 0) { 
      if (this.c === 1) { 
        if (output === "") { output += "j" } else { output += "+j"}
      } else if (this.c > 1) { 
        output += "+" + `${this.c}j` 
      } else if (this.c === -1) { 
        output += "-j" 
      } else { output += `${this.c}j` }
    };

    
    if (this.d !== 0) { 
      if (this.d === 1) { 
        if (output === "") { output += "k" } else { output += "+k"}
      } else if (this.d > 1) { 
        output += "+" + `${this.d}k` 
      } else if (this.d === -1) { 
        output += "-k" 
      } else { output += `${this.d}k` }
    };

    return output || "0";
  }
}