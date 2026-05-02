class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector <vector<bool>> visited(m, vector<bool> (n, false));

        queue <pair<int,int>> q;

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 0) {
                    q.push({r, c});
                    visited[r][c] = 1;
                }
            }
        }

        vector <vector <int> > dirs{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        while (!q.empty()) {
            auto cur = q.front(); q.pop();
            int r = cur.first, c = cur.second;

            for (auto dir: dirs) {
                int nr = r + dir[0];
                int nc = c + dir[1];

                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                if (grid[nr][nc] == -1 || visited[nr][nc]) continue;

                q.push({nr, nc});
                visited[nr][nc] = 1;
                grid[nr][nc] = min(grid[nr][nc], grid[r][c] + 1);
            }
        }
    }
};
