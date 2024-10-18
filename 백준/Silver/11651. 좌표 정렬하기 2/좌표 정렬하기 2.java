import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        List<Integer[]> arr = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String[] input = br.readLine().split(" ");
            Integer[] intArr = Arrays.stream(input)
                    .map(Integer::parseInt)
                    .toArray(Integer[]::new);

            arr.add(intArr);
        }

        arr.sort((a, b) -> {
           int compare = a[1].compareTo(b[1]);
           if (compare == 0) {
               return a[0].compareTo(b[0]);
           }
           return compare;
        });

        for (Integer[] elem : arr) {
            System.out.println(elem[0] + " " + elem[1]);
        }
    }
}