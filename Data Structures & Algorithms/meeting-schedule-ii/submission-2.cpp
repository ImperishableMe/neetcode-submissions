/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {        
        sort(intervals.begin(), intervals.end(), [](auto &a, auto &b)->bool {
            return a.start < b.start;
        });
        priority_queue <int, vector<int>, greater<int>> pq;
        pq.push(INT_MIN);
        int ans = 0;
        for (auto [st, en]: intervals) {
            auto earliest = pq.top(); 
            if (earliest <= st) {
                pq.pop();    
            }
            pq.push(en);
            ans = max(ans, (int)pq.size());
        }
        return ans;
    }
};
