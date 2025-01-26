import java.io.*;
import java.util.*;

public class Main {
    static FastReader scan = new FastReader();
    static PrintWriter out = new PrintWriter(System.out);

    private static int timeToSeconds(String time) {
        String[] parts = time.split(":");
        int hours = Integer.parseInt(parts[0]);
        int minutes = Integer.parseInt(parts[1]);
        int seconds = Integer.parseInt(parts[2]);
        return hours * 3600 + minutes * 60 + seconds;
    }

    private static String secondsToTime(int sec) {
        int hours = sec / 3600;
        int minutes = (sec % 3600) / 60;
        int seconds = sec % 60;
        return String.format("%02d:%02d:%02d", hours, minutes, seconds);
    }

    public static void main(String[] args) throws IOException {
        String currTime = scan.nextLine();
        String targetTime = scan.nextLine();

        // 초 단위로 변환
        int currTimeSec = timeToSeconds(currTime);
        int targetTimeSec = timeToSeconds(targetTime);

        if (currTimeSec < targetTimeSec) {
            out.println(secondsToTime(targetTimeSec - currTimeSec));
        } else {
            out.println(secondsToTime(targetTimeSec + 24 * 60 * 60 - currTimeSec));
        }

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
