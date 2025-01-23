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

    private static long A;
    private static long B;
    private static long C;

    static void input() {
        FastReader scan = new FastReader();
        A = scan.nextLong();
        B = scan.nextLong();
        C = scan.nextLong();
    }

    public static void main(String[] args)  {
        input();

        System.out.println(A + B + C);
    }
}
