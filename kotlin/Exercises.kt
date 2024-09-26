import java.io.BufferedReader
import java.io.FileReader
import java.io.IOException

fun change(amount: Long): Map<Int, Long> {
    require(amount >= 0) { "Amount cannot be negative" }
    
    val counts = mutableMapOf<Int, Long>()
    var remaining = amount
    for (denomination in listOf(25, 10, 5, 1)) {
        counts[denomination] = remaining / denomination
        remaining %= denomination
    }
    return counts
}

// Write your first then lower case function here
fun firstThenLowerCase(a: List<String>, p: (String) -> Boolean): String? {
    return a.firstOrNull(p)?.lowercase()
}

// Write your say function here


// Write your meaningfulLineCount function here
fun meaningfulLineCount(fileName: String): Long {
    var count = 0L;

    try {
        FileReader(fileName).use { fileReader ->
            BufferedReader(fileReader).use { bufferedReader ->
                bufferedReader.forEachLine { line ->
                    if (!line.trim().isEmpty()) {
                        if (!(line.trim()[0] == '#')) {
                            count += 1L
                        }
                    }
                }
            }
            return count
        }
    } catch (e: IOException) {
        throw IOException("No such file")
    }
}

// Write your Quaternion data class here

// Write your Binary Search Tree interface and implementing classes here
