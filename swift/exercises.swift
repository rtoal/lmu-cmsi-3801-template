import Foundation

struct NegativeAmountError: Error {}
struct NoSuchFileError: Error {}

func change(_ amount: Int) -> Result<[Int:Int], NegativeAmountError> {
    if amount < 0 {
        return .failure(NegativeAmountError())
    }
    var (counts, remaining) = ([Int:Int](), amount)
    for denomination in [25, 10, 5, 1] {
        (counts[denomination], remaining) = 
            remaining.quotientAndRemainder(dividingBy: denomination)
    }
    return .success(counts)
}

// Write your first then lower case function here
// test cases require 'satisfying' instead of '_'
func firstThenLowerCase(of array: [String], satisfying predicate: (String) -> Bool) -> String? {
    return array.first(where: predicate)?.lowercased()
}


struct Say {
    private var words: [String]
    init(_ word: String = "") {
        //self.words = word.isEmpty ? [] : [word]
        self.words = [word]
    }
    func and(_ word: String) -> Say {
        var newSay = self
        newSay.words.append(word)
        return newSay 
    }
    var phrase: String {
        return words.joined(separator: " ") 
    }
}
func say(_ word: String = "") -> Say {
    return Say(word)
}

/*
// Write your meaningfulLineCount function here
enum FileError: Error {
    case fileNotFound
    case failedToRead
}

func meaningfulLineCount(_ filename: String) async -> Result <Int, Error> {
    
    do {

        let fileURL = URL(fileURLWithPath: filename)

        guard FileManager.default.fileExists(atPath: filename) else {
            return .failure(FileError.fileNotFound)
        }

    var lineCount = 0

    for try await line in fileURL.lines {
        let trimmedLine = line.trimmingCharacters(in: .whitespaces)

        if !trimmedLine.isEmpty && !trimmedLine.hasPrefix("#") {
            lineCount += 1
            }
        }

        return .success(lineCount)

    } catch { 

    return .failure(FileError.failedToRead)
    }
}
*/
// Write your Quaternion struct here

struct Quaternion: CustomStringConvertible {
    let a: Double // scalar
    let b: Double // i
    let c: Double // j
    let d: Double // k

    init(a: Double? = 0, b: Double? = 0, c: Double? = 0, d: Double? = 0) {
        self.a = a ?? 0
        self.b = b ?? 0
        self.c = c ?? 0
        self.d = d ?? 0
    }

    var coefficients: [Double] {
        return [a, b, c, d]
    }

    var conjugate: Quaternion {
        return Quaternion(
            a: a,
            b: -b,
            c: -c,
            d: -d
        )
    }

    var description: String {
	    var components: [String] = []
		if a != 0 {
			components.append("\(a)")
		}
		if b != 0 {
            if b == 1 {
                components.append("+i")
            } else if b == -1 {
                components.append("-i")
            } else if b > 0 {
			    components.append("+\(b)i")
		    } else {
                components.append("\(b)i")
            }
        } 
		if c != 0 {
            if c == 1 {
                components.append("+j")
            } else if c == -1 {
                components.append("-j")
            } else if c > 0 {
			    components.append("+\(c)j")
		    } else {
                components.append("\(c)j")
            }
        } 
        if d != 0 {
            if d == 1 {
                components.append("+k")
            } else if d == -1 {
                components.append("-k")
            } else if d > 0 {
			    components.append("+\(d)k")
		    } else {
                components.append("\(d)k")
            }
        }    
    
        if components.isEmpty {
            return "0"
        }

        var result = components.joined()
        if result.first == "+" {
            result.removeFirst()
        }
        
        return result
    }

    static func == (lhs: Quaternion, rhs: Quaternion) -> Bool {
        return (lhs.a == rhs.a && // scalar1 = scalar2?
                lhs.b == rhs.b && // i1 = i2?
                lhs.c == rhs.c && // j1 = j2?
                lhs.d == rhs.d)  // k1 = k2?
    }

    static var ZERO: Quaternion {
        return Quaternion(
            a: 0, // scalar
            b: 0, // i
            c: 0, // j
            d: 0  // k
        )
    }

    static var I: Quaternion {
        return Quaternion(
            a: 0, // scalar
            b: 1, // i
            c: 0, // j
            d: 0  // k
        )
    }

    static var J: Quaternion {
        return Quaternion(
            a: 0, // scalar
            b: 0, // i
            c: 1, // j
            d: 0  // k
        )
    }

    static var K: Quaternion {
        return Quaternion(
            a: 0, // scalar
            b: 0, // i
            c: 0, // j
            d: 1  // k
        )
    }
}

func + (lhs: Quaternion, rhs: Quaternion) -> Quaternion {
    return Quaternion(
        a: lhs.a + rhs.a, 
        b: lhs.b + rhs.b, 
        c: lhs.c + rhs.c,
        d: lhs.d + rhs.d
    )
}

func * (lhs: Quaternion, rhs: Quaternion) -> Quaternion {
    return Quaternion(
        a: (lhs.a * rhs.a) - (lhs.b * rhs.b) - (lhs.c * rhs.c) - (lhs.d * rhs.d),
        b: (lhs.a * rhs.b) + (lhs.b * rhs.a) + (lhs.c * rhs.d) - (lhs.d * rhs.c),
        c: (lhs.a * rhs.c) - (lhs.b * rhs.d) + (lhs.c * rhs.a) + (lhs.d * rhs.b),
        d: (lhs.a * rhs.d) + (lhs.b * rhs.c) - (lhs.c * rhs.b) + (lhs.d * rhs.a) 
    )
}

// Write your Binary Search Tree enum here


enum BinarySearchTree {
    case empty
    indirect case node(BinarySearchTree, String, BinarySearchTree)

    var size: Int {
        switch self {
        case .empty:
            return 0
        case let .node(left, _, right):
            return left.size + 1 + right.size
        }
    }

    func insert(_ newValue: String) -> BinarySearchTree {
        switch self {
        case .empty:
            return .node(.empty, newValue, .empty)
        case let .node(left, value, right):
            if newValue < value {
                return .node(left.insert(newValue), value, right)
            } else if newValue > value {
                return .node(left, value, right.insert(newValue))
            } else {
                return self
            }
        }
    }

    func contains(_ searchValue: String) -> Bool {
        switch self {
        case .empty:
            return false
        case let .node(left, value, right):
            if searchValue == value {
                return true
            } else if searchValue < value {
                return left.contains(searchValue)
            } else {
                return right.contains(searchValue)
            }
        }
    }

    

}