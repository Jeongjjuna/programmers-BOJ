import java.io.*;
import java.util.*;

public class Main {
    private static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        FastReader scan = new FastReader(reader);

        N = scan.nextInt();

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            int a = scan.nextInt();
            int b = scan.nextInt();
            sb.append(a + b).append("\n");
        }

        System.out.println(sb);
    }

    static void input() {
    }

    static class FastReader {
        private final BufferedReader reader;
        private final StreamTokenizer tokenizer;

        public FastReader(BufferedReader reader) {
            this.reader = reader;
            this.tokenizer = new StreamTokenizer(reader);
        }

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
    }

}
