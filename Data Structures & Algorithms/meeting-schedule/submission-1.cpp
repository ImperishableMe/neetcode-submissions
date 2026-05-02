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
        /*
        -> weak ordering

        */
        auto cmp = [](Interval a, Interval b)->bool{
            if (a.end == b.end) return a.start < b.start;
            return a.end < b.end;
        };

        sort(intervals.begin(), intervals.end(), cmp);
        int right_border = -1;
        for (auto interval: intervals) {
            if (interval.start < right_border) {
                return false;
            }
            right_border = max(right_border, interval.end);
        }
        return true;
    }
};
