import java.io.*;
import java.util.*;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final StringBuilder sb = new StringBuilder();

    static int A;
    static int B;

    static void input() throws IOException {
        String[] tokens = br.readLine().split(" ");
        A = Integer.parseInt(tokens[0]);
        B = Integer.parseInt(tokens[1]);
    }

    public static void main(String[] args) throws Exception {
        input();

        System.out.println(A + B);
    }
}