struct DSU {
    int n;
    vector <int> par, sz;

    DSU (int _n) {
        this->n = _n;
        par.resize(n);
        sz.resize(n);
        for (int i = 0; i < n; i++) {
            par[i] = i;
            sz[i] = 1;
        }
    }

    int Find(int u) {
        if (par[u] != u) {
            par[u] = Find(par[u]);
        }
        return par[u];
    }

    bool Union(int u, int v) {
        u = Find(u);
        v = Find(v);
        if (u == v) return false;
        if (sz[u] < sz[v]) swap(u, v);
        sz[u] += sz[v];
        par[v] = u;
        return true;
    }
};

class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        DSU dsu(n);
        int comps = n;
        for (auto edge: edges) {
            int u = edge[0], v = edge[1];
            comps -= dsu.Union(u, v);
        }
        return comps;
    }
};
