class Solution {
    vector <vector <int>> adj;
    vector <bool> visited;
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        adj.assign(n, vector<int> ());
        visited.assign(n, false);

        for (auto edge: edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }
        int count = 0;

        auto bfs = [&](int x) {
            queue <int> q;
            q.push(x);
            visited[x] = 1;
            
            while (!q.empty()) {
                int u = q.front(); q.pop();
                for (auto v : adj[u]) {
                    if (!visited[v]) {
                        visited[v] = 1;
                        q.push(v);
                    }
                }
            }
        };

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                count++;
                bfs(i);
            }
        }
        return count;
    }
};
