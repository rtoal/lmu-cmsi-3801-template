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
        self.words = word.isEmpty ? [] : [word]
    }
    func and(_ word: String) -> Say {
        var newSay = 
        newSay.words.append(word)
        return newSay 
    }
    var phrase: String {
        return words.joined(separator: " ") 
    }
}
func say(_ word: String = "") -> Say {
    return Say(word)


// Write your meaningfulLineCount function here
enum FileError: Error {
    case fileNotFound
    case failedToRead
}

func meaningfulLineCount(_ filename: String) async -> Result<Int, Error> {
    
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

// Write your Quaternion struct here

// Write your Binary Search Tree enum here

/*
enum BST {
    case empty
    indirect case node(BST, String, BST)

    var size Int {
        case .empty: return 0

        // pattern match to check the left and right nodes and let indicates that there is a pattern
        case let .node(left, _, right): return left.size + 1 + right.size
    }

}

var t = BST(BST.node(BST.empty), 1, BST.empty),
2,
BST.node(BST.empty, 3, BST.empty)
*/