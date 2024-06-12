import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        
        // 신고기록 : Hash<String, Set<String>> = {신고자1 : {받은사람1, 받은사람2, 받은사람3}}
        // 신고당한 기록 : Hash<String, Integer> = {사람1 : 1, 사람2 : 5, 사람3 : 7}
        // 신고당한 기록을 순회하며 k번 이상인 사람을 찾는다. 정지된 ID = [사람1, 사람2, 사람3]
        
        // 신고기록 구하기
        Map<String, Set<String>> reportLog = new HashMap<>();
        for (String id : id_list) {
            reportLog.put(id, new HashSet<>());
        }
        
        
        Map<String, Integer> reportCount = new HashMap<>();
        for (String r : report) {
            String[] fromAndTo = r.split(" ");
            String from = fromAndTo[0];
            String to = fromAndTo[1];
            

            reportCount.putIfAbsent(to, 0);
            
            // reportLog에 없는 경우에만 카운트를 올려준다.
            if (!reportLog.get(from).contains(to)) {
                reportLog.get(from).add(to);
                reportCount.put(to, reportCount.get(to) + 1);
            }   
        }
        
        
        
        Set<String> reported = new HashSet<>();
        for (Map.Entry<String, Integer> entry : reportCount.entrySet()) {
            if (k <= entry.getValue()) {
                reported.add(entry.getKey());
            }
        }
        
        int[] answer = new int[id_list.length];

        
//         System.out.println(reportLog);
//         System.out.println(reportCount);
//         System.out.println(reported);
        
        for (int i = 0; i < id_list.length; i++) {
            int cnt = 0;
            
            for (String target : reportLog.get(id_list[i])) {
                if (reported.contains(target)) {
                    cnt += 1;
                }
            }
            
            answer[i] = cnt;
        }


        return answer;
    }
}