struct DSU {
    int n;
    vector <int> par, sz;
    DSU (int _n) {
        this->n = _n;
        par.resize(n), sz.resize(n);
        for (int i = 0; i < n; i++) {
            par[i] = i;
            sz[i] = 1;
        }
    }

    int Find(int u) {
        if (u != par[u]) {
            par[u] = Find(par[u]);
        }
        return par[u];
    }

    bool Union(int u, int v) {
        u = Find(u);
        v = Find(v);
        if (u == v) return false;
        if (sz[u] < sz[v]) swap(u, v);
        par[v] = u;
        sz[u] += sz[v];
        return true;
    }
};

class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        // DSU d(n);
        if (edges.size() + 1 != n) return false;
        DSU d(n);

        for (auto edge: edges) {
            int u = edge[0], v = edge[1];
            if (!d.Union(u, v)) {
                return false;
            }
        }
        return true;
    }
};
