import java.util.*;

class Solution {
    
    private int[] dxs = {-1, 0, 1, 0};
    private int[] dys = {0, 1, 0, -1};
    
    private boolean isRange(int[][] maps, int nx, int ny) {
        return 0 <= nx && nx < maps.length && 0 <= ny && ny < maps[0].length;
    }
    
    private boolean canGo(int[][] maps, int[][] visited, int nx, int ny) {
        if (isRange(maps, nx, ny)) { // 범위
            if (visited[nx][ny] == 0) { // 이전에 방문했는지
                if (maps[nx][ny] == 1) { // 벽이 아닌지
                    return true;
                }
            }
        }
        return false;   
    }
    
    private void bfs(int[][] maps, int[][] visited, int s, int e) {
        
        Queue<int[]> q = new LinkedList<>(); // offer, poll
        q.offer(new int[]{s, e});
        while (!q.isEmpty()) {
            int[] point = q.poll();
            int x = point[0];
            int y = point[1];
            
            for (int i = 0; i < 4; i++) {
                int nx = x + dxs[i];
                int ny = y + dys[i];
                
                if (canGo(maps, visited, nx, ny)) {
                    visited[nx][ny] = visited[x][y] + 1;
                    q.offer(new int[]{nx, ny});
                }
            }
        }
    }
    
    public int solution(int[][] maps) {
        
        int n = maps.length;
        int m = maps[0].length;
        
        // 최단거리 탐색
        int[][] visited = new int[n][m];
        visited[0][0] = 1;
        bfs(maps, visited, 0, 0);
                
        // 최단거리 조회
        if (visited[n - 1][m - 1] == 0) {
            return -1;
        }
        return visited[n - 1][m - 1];
    }
}