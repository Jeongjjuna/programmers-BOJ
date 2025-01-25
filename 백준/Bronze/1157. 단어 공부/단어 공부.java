import java.io.*;
import java.util.*;

public class Main {
    static FastReader scan = new FastReader();
    static PrintWriter out = new PrintWriter(System.out);

    private static String str;

    public static void main(String[] args) throws IOException {
        str = scan.nextLine();

        // 전부 대문자로 변경
        str = str.toUpperCase();

        // 알파벳 카운트
        int[] count = new int[26];
        for(char c : str.toCharArray()) {
            count[c - 'A'] += 1;
        }

        int maxCount = Arrays.stream(count)
                        .max()
                        .getAsInt();
        List<Character> candidates = new ArrayList<>();
        for (int i = 0; i < 26; i++) {
            if (count[i] == maxCount)
                candidates.add((char)('A' + i));
        }

        if (candidates.size() > 1)
            out.println("?");
        else
            out.println(candidates.get(0));

        scan.close();
        out.close();
    }

    static class FastReader {
        private final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        private final StreamTokenizer tokenizer = new StreamTokenizer(reader);

        public String nextString() throws IOException {
            tokenizer.nextToken();
            return tokenizer.sval;
        }

        public int nextInt() throws IOException {
            tokenizer.nextToken();
            return (int) tokenizer.nval;
        }

        public String nextLine() throws IOException {
            return reader.readLine();
        }

        void close() throws IOException {
            reader.close();
        }
    }
}
