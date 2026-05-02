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
        map <int,int> diff;
        for (auto [st, en]: intervals) {
            diff[st]++;
            diff[en]--;
        }
        int sum = 0, ans = 0;

        for (auto [k, v]: diff) {
            sum += v;
            ans = max(ans, sum);
        }
        return ans;

    }
};
