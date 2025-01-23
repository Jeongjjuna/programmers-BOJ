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

    private static int N;

    static void input() {
        FastReader scan = new FastReader();
        N = scan.nextInt();
    }

    public static void main(String[] args)  {
        input();

        String star = "*";
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < N + 1; i++) {
            sb.append(star.repeat(i) + "\n");
        }
        System.out.println(sb);
    }
}
