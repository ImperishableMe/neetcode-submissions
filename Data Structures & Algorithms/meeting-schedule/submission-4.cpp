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
    bool canAttendMeetings(vector<Interval>& intervals) {
        sort (intervals.begin(), intervals.end(), [](auto &a, auto &b)->bool {
            return a.end < b.end;
        });

        int right = -1;
        for (auto interval: intervals) {
            int l = interval.start, r = interval.end;
            if (l < right) return false;
            else {
                right = max(right, r);
            }
        }
        return true;
    }
};
