class Solution {
public:

    string encode(vector<string>& strs) {
        string enc;
        for (auto str: strs) {
            enc += to_string(str.size());
            enc += "_";
            enc += str;
        }
        cout << enc << endl;
        return enc;
    }

    vector<string> decode(string s) {
        cout << s << endl;
        vector <string> code;
        int len = 0, i = 0;
        while(i < s.size()) {
            int j = i;
            while (j < s.size() && isdigit(s[j])) len = len * 10 + (s[j++] - '0');
            j++;
            code.push_back(s.substr(j, len));
            i = j + len;
            // cout << "end: " << i << endl;
            len = 0;
        }
        return code;
    }
};
