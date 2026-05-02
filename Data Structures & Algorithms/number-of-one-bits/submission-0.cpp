class Solution {
public:
    int hammingWeight(uint32_t n) {
        int one_bits = 0;
        while (n) {
            int cur_bit = n & 1;
            one_bits += cur_bit == 1;
            n >>= 1;
        }
        return one_bits;
    }
};
