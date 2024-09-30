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
import java.util.ArrayList;

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
record Quaternion(double a, double b, double c, double d) {

    public final static Quaternion ZERO = new Quaternion(0, 0, 0, 0);
    public final static Quaternion I = new Quaternion(0, 1, 0, 0);
    public final static Quaternion J = new Quaternion(0, 0, 1, 0);
    public final static Quaternion K = new Quaternion(0, 0, 0, 1);

    Quaternion plus(Quaternion other) {
        return new Quaternion(a + other.a, b + other.b, c + other.c, d + other.d);
    }

    Quaternion times(Quaternion other) {
        return new Quaternion(
            a * other.a - b * other.b - c * other.c - d * other.d,
            a * other.b + b * other.a + c * other.d - d * other.c,
            a * other.c - b * other.d + c * other.a + d * other.b,
            a * other.d + b * other.c - c * other.b + d * other.a);
    }
    public Quaternion conjugate() {
        return new Quaternion(a, -b, -c, -d);
    }

    public List<Double> coefficients() {
        return List.of(a, b, c, d);
    }

    public String toString() {
        List<String> terms = new ArrayList<>();

        if (a != 0.0) terms.add(String.valueOf(a));
        if (b != 0.0) terms.add((b == 1.0 ? "" : b == -1.0 ? "-" : String.valueOf(b)) + "i");
        if (c != 0.0) terms.add((c == 1.0 ? "" : c == -1.0 ? "-" : String.valueOf(c)) + "j");
        if (d != 0.0) terms.add((d == 1.0 ? "" : d == -1.0 ? "-" : String.valueOf(d)) + "k");

        if (terms.isEmpty()) {
            return "0";
        } else if (terms.size() == 1) {
            return terms.get(0);
        } else {
            StringBuilder result = new StringBuilder();
            for (int i = 0; i < terms.size(); i++) {
                if (i > 0) {
                    result.append("+");
                }
                result.append(terms.get(i));
            }
            return result.toString().replace("+-", "-");
        }
    }
}

// Write your BinarySearchTree sealed interface and its implementations here
sealed interface BinarySearchTree permits Empty, Node {
    int size();
    boolean contains(String value);
    BinarySearchTree insert(String value);
}

final record Empty() implements BinarySearchTree {
    @Override
    public int size() {
        return 0;
    }

    @Override
    public boolean contains(String value) {
        return false;
    }

    @Override
    public BinarySearchTree insert(String value) {
        return new Node(value, this, this);
    }

    @Override
    public String toString() {
        return "()";
    }
}

final class Node implements BinarySearchTree {
    private final String value;
    private final BinarySearchTree left;
    private final BinarySearchTree right;

    Node(String value, BinarySearchTree left, BinarySearchTree right) {
        this.value = value;
        this.left = left;
        this.right = right;
    }

    @Override
    public int size() {
        return 1 + left.size() + right.size();
    }

    @Override
    public boolean contains(String value) {
        return this.value.equals(value) || left.contains(value) || right.contains
        (value);
    }

    @Override
    public BinarySearchTree insert(String value) {
        if (value.compareTo(this.value) < 0) {
            return new Node(this.value, left.insert(value), right);
        } else {
            return new Node(this.value, left, right.insert(value));
        }
    }

    @Override
    public String toString() {
        String leftString = left instanceof Empty ? "" : left.toString();
        String rightString = right instanceof Empty ? "" : right.toString();
        return "(" + leftString + value + rightString + ")";
    }
}
