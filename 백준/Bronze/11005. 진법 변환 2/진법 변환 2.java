import java.io.*;
import java.util.*;

public class Main {
    static FastReader scan = new FastReader();
    static PrintWriter out = new PrintWriter(System.out);

    static long N;
    static int B;

    public static char convert(int num) {
        if (num < 10) {
            return (char) ('0' + num);
        }
        return (char) ('A' + (num - 10));
    }

    public static void main(String[] args) {
        N = scan.nextLong();
        B = scan.nextInt();

        // N -> B진법
        List<Integer> reverseAnswer = new ArrayList<>();
        while(B <= N) {
            int mode = (int) N % B;
            reverseAnswer.add(mode);
            N = N / B;
        }
        reverseAnswer.add((int) N);

        for (int i = reverseAnswer.size() - 1; i > -1; i--) {
            int num = reverseAnswer.get(i);
            out.print(convert(num));
        }

        // 자원 해제
        scan.close();
        out.close();
    }


    static class FastReader {
        private final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        private StringTokenizer tokenizer;

        String nextString() {
            while (tokenizer == null || !tokenizer.hasMoreElements()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return tokenizer.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(nextString());
        }

        long nextLong() {
            return Long.parseLong(nextString());
        }

        String nextLine() {
            String str = "";
            try {
                str = reader.readLine();
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
            return str;
        }

        void close() {
            try {
                reader.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
