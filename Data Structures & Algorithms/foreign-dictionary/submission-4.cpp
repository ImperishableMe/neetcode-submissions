class Solution {
    unordered_map <char, vector<char>> adj;
    unordered_map <char, int> visited;
public:
    string foreignDictionary(vector<string>& words) {
        int n = words.size();
        int ec = 0;
        set <char> charset;

        for (auto word: words) {
            charset.insert(word.begin(), word.end());
        }

        auto is_valid = [&](string &s1, string &s2) {
            int sz = min(s1.size(), s2.size());

            for (int i = 0; i < sz; i++) {
                if (s1[i] != s2[i]) {
                    return true;
                }
            }
            return s1.size() <= s2.size();
        };

        for (int i = 0; i + 1 < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (!is_valid(words[i], words[j])) {
                    return "";
                }
            }
        }



        auto create_edge = [&](string &s1, string &s2) {
            int sz = min(s1.size(), s2.size());

            for (int i = 0; i < sz; i++) {
                if (s1[i] != s2[i]) {
                    adj[s1[i]].emplace_back(s2[i]);
                    // ec++;
                    return;
                }
            }
        };
        for (int i = 0; i + 1 < words.size(); i++) {
            create_edge(words[i], words[i+1]);
        }
        int sz = adj.size();
        
        string order;
        for (auto k: charset) {
            // char k = it->first;
            if (!visited[k] && !dfs(k, order)) {
                return "";
            }
        }
        reverse(order.begin(), order.end());
        return order;
    }

    bool dfs(char u, string &order) {
        visited[u] = 1;
        for (auto v: adj[u]) {
            // cout << u << " " << v << endl;
            if (visited[v] == 1) return false;
            if (!visited[v] && !dfs(v, order)) return false;
        }
        visited[u] = 2;
        order += u;
        return true;
    }
};
