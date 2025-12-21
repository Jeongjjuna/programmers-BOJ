import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int N, S, ANS = 0;
    private static Integer[] ARR;

    private static List<Integer> visited = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        String[] input = br.readLine().split(" ");
        N = Integer.parseInt(input[0]);
        S = Integer.parseInt(input[1]);
        ARR = Arrays.stream(br.readLine().split(" "))
                .map(Integer::parseInt)
                .toArray(Integer[]::new);

        // ARR 를 백트래킹으로 탐색해보자.
        int idx = 0;
        int sum = 0; // 현재까지 부분수열 합
        boolean isPossible = false;
        dfs(idx, sum, isPossible);

        System.out.println(ANS);
    }

    private static void dfs(int idx, int sum, boolean isPossible) {
        if (visited.size() == N) {
            if (!isPossible) return;

            if (sum == S) {
                ANS += 1;
            }
            return;
        }

        // idx 가 부분수열에 포함
        visited.add(1);
        dfs(idx + 1, sum + ARR[idx], true);
        visited.remove(visited.size() - 1);

        // idx 가 부분수열에 미포함
        visited.add(0);
        dfs(idx + 1, sum, isPossible);
        visited.remove(visited.size() - 1);
    }
}
