import java.io.*;
import java.util.*;

public class Main {
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

    private static final String EMPTY = " ";
    private static final String STAR = "*";
    private static int N;

    static void input() {
        FastReader scan = new FastReader();
        N = scan.nextInt();
    }

    public static void main(String[] args)  {
        input();

        StringBuilder sb = new StringBuilder();
        for (int idx = 1; idx <= N; idx++) {
            sb.append(EMPTY.repeat(N - idx));
            sb.append(STAR.repeat(idx));
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
