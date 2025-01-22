class Solution {
    private int[][] map;
    private int[] dxs = {0, 1, 0, -1};
    private int[] dys = {1, 0, -1, 0}; // 동, 남, 서, 북
    private int x = 0;
    private int y = 0;
    private int dire = 0;
    private int num = 1;
    
    public int[][] solution(int n) {
        // 변수 입력 및 선언
        map = new int[n][n];
        
        while (num < (n * n) + 1) {
            map[x][y] = num; 
            
            int[] next_xy = next(n);
            x = next_xy[0];
            y = next_xy[1];
            num += 1;
        }
        
        return map;
    }
    
    // 갈 수 있는지 확인
    private boolean canGo(int nx, int ny, int n) {
        // 1. n * n 격자내에 있어야 한다.
        if (0 <= nx &&  nx < n && 0 <= ny && ny < n) {
            // 2. 아직 방문하지 않은 위치여야한다.
            if (map[nx][ny] == 0) {
                return true;
            }
        }
        // 갈수 없음.
        return false;
    }
    
    // 다음 위치를 반환한다.
    private int[] next(int n) {
        int nx = x + dxs[dire];
        int ny = y + dys[dire];
        
        if (canGo(nx, ny, n)) {
            return new int[] {nx, ny};
        }
        dire = (dire + 1) % 4;
        return new int[] {x + dxs[dire], y + dys[dire]};
    }
}