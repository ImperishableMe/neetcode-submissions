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

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                count++;
                dfs(i);
            }
        }
        return count;
    }

    void dfs(int u) {
        visited[u] = 1;
        for (auto v: adj[u]) {
            if (!visited[v]) {
                // cout << u << " -> " << v << endl; 
                dfs(v);
            }
        }
    }
};
