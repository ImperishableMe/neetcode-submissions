class Solution {
public:

    string encode(vector<string>& strs) {
        string ans;
        for (auto str: strs) {
            ans += to_string(str.size());
            ans += "_";
            ans += str;
        }
        cout << ans << endl;
        return ans;
    }

    vector<string> decode(string s) {
        vector <string> decodes;
        for (int i = 0; i < s.size(); ) {
            int len = 0;
            int j = i;
            while (j < s.size() && isdigit(s[j])) {
                len = len * 10 + (s[j] - '0');
                j++;
            }
            j++; // ignore _
            decodes.push_back(s.substr(j, len));
            // cout << s.substr(j, len) << endl;
            j += len;
            i = j;
        }
        return decodes;
    }
};
