import java.io.*;
import java.util.*;

public class Main {
    private static int N;

    public static void main(String[] args) {
        FastReader scan = new FastReader();
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
        private final BufferedReader br;
        private StringTokenizer st;

        public FastReader() {
            this.br = new BufferedReader(new InputStreamReader(System.in));
        }

        String nextString() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return st.nextToken();
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
                str = br.readLine();
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
            return str;
        }
    }
}
