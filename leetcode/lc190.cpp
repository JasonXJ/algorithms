#include <cstdint>

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t rv = 0;
        for (int i = 0; i < 32; i++) {
            rv <<= 1;
            rv |= n & 1;
            n >>= 1;
        }
        return rv;
    }
};
