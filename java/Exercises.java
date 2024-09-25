import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.Optional;
import java.util.function.Predicate;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.stream.Stream;

public class Exercises {
    static Map<Integer, Long> change(long amount) {
        if (amount < 0) {
            throw new IllegalArgumentException("Amount cannot be negative");
        }
        var counts = new HashMap<Integer, Long>();
        for (var denomination : List.of(25, 10, 5, 1)) {
            counts.put(denomination, amount / denomination);
            amount %= denomination;
        }
        return counts;
    }

    // Write your firstThenLowerCase function here
    public static Optional<String> firstThenLowerCase(List<String> a, Predicate<String> p) {
        return a.stream()
                .filter(p)
                .findFirst()
                .map(String::toLowerCase);
    }

    // Write your say function here
    public interface SayObject {
        SayObject and(String next);
        String phrase();
    }
    
    public static SayObject say() {
        return say("");
    }
    
    public static SayObject say(String initial) {
        return new SayObjectImpl(initial);
    }
    
    private static class SayObjectImpl implements SayObject {
        private final StringBuilder phrase;
    
        private SayObjectImpl(String initial) {
            this.phrase = new StringBuilder(initial != null ? initial : "");
        }
    
        @Override
        public SayObject and(String next) {
            if (next != null) {
                StringBuilder newPhrase = new StringBuilder(phrase);
                newPhrase.append(" ");
                newPhrase.append(next);
                return new SayObjectImpl(newPhrase.toString());
            }
            return this;
        }
    
        @Override
        public String phrase() {
            return phrase.toString();
        }
    }

    // Write your line count function here
    public static long meaningfulLineCount(String filename) throws IOException {
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            return reader.lines()
                .filter(line -> !line.trim().isEmpty() && !line.trim().startsWith("#"))
                .count();
        } catch (FileNotFoundException e) {
            throw new FileNotFoundException("No such file");
        }
    }
}
// Write your Quaternion record class here

// Write your BinarySearchTree sealed interface and its implementations here
