/* Let's say we have a function f(n) \in {'f', 's'} such that f(n) ==
 * 'f' iff the first player must win, and f(n) == 's' iff the second
 * player must win. It is obviously that f(0) = 's', f(1) = 'f', f(2)
 * = 'f'. Given this base cases, we can easily compute f(n) for any n:
 *
 * f(n) = (f(n-1) == 's' or f(n-2) == 's' or f(n-3) == 's')?'f':'s'.
 *
 * This formula gives us an easy way to implement an O(n) solution by
 * using a recursive function.  However, actually, we do not need to
 * compute this function at all, which yield an O(1) solution. Let's
 * compute the value of f(n) for n \in [0, 7]:
 *
 *       n: 0 1 2 3 4 5 6 7
 *    f(n): s f f f s f f f
 * 
 * We should notice that the sequence is 'sfff' repeating itself
 * twice. So, f(n) can actually be computed as f(n) = (n % 4 ==
 * 0)?'s':'f'.
 */
class Solution {
public:
    bool canWinNim(int n) {
        return n % 4 != 0;
    }
};
