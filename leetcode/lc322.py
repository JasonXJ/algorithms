from math import isinf


# This solution is copied from https://discuss.leetcode.com/topic/32589/fast-python-bfs-solution/2
class CopiedSolution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        value1 = [0]
        value2 = []
        nc =  0
        visited = [False]*(amount+1)
        visited[0] = True
        while value1:
            nc += 1
            for v in value1:
                for coin in coins:
                    newval = v + coin
                    if newval == amount:
                        return nc
                    elif newval > amount:
                        continue
                    elif not visited[newval]:
                        visited[newval] = True
                        value2.append(newval)
            value1, value2 = value2, []
        return -1


# A DFS+DP+Pruning solution (Still not fast enough and get TLE error)
class Solution(object):
    def coinChange(self, coins, amount):
        assert amount >= 0
        if amount == 0:
            return 0
        if len(coins) == 0:
            return -1
        INF = float('+inf')
        sorted_coins = sorted(coins, reverse=True)
        largest_coin = sorted_coins[0]

        # ``dp_ncoins[x]`` is the minimal number of coins needed to make up
        # amount `x`. ``dp_lower_bound[x]`` is the lower bound (inclusive) of
        # the minimal number of coins.
        dp_ncoins = {x:1 for x in coins}
        dp_lower_bound = {}


        def calc_minimum_coins(current_amount, max_ncoins_allow=amount):
            """ `max_ncoins_allow` is a parameter for pruning. That is to say,
            if at some point we know that ``minimal_coins(current_amount) >
            max_ncoins_allow``, than we will stop the searching.
        
            The return value is a pair ``(search_finished, minimum coins or
            lower bound)``, so possible return values are:

            - ``(True, minimal coins)`` if the minimal number of coins is found
            - ``(True, -1)`` if cannot make the amount up
            - ``(False, lower_bound)`` if `max_ncoins_allow` is reached so the
              search ends prematurely and only a lower bound is found.
            """

            try:
                return (True, dp_ncoins[current_amount])
            except KeyError:
                pass
            lower_bound = dp_lower_bound.get(current_amount)
            if lower_bound is None:
                lower_bound = (current_amount + largest_coin - 1) // largest_coin
            if lower_bound > max_ncoins_allow:
                return (False, lower_bound)

            sub_max_ncoins_allow = max_ncoins_allow - 1
            sub_min_ncoins = INF
            sub_min_lower_bound = INF
            for coin in sorted_coins:
                if coin > current_amount:
                    continue
                # Note that now ``coin < current_amount`` because if ``coin ==
                # current_amount``, `dp_ncoins` will have the entry and we will
                # never reach here.
                sub_result = calc_minimum_coins(current_amount - coin, sub_max_ncoins_allow)
                if sub_result[0]:
                    sub_ncoins = sub_result[1]
                    if sub_ncoins != -1 and sub_ncoins < sub_min_ncoins:
                        sub_min_ncoins = sub_ncoins
                        sub_max_ncoins_allow = sub_min_ncoins - 1
                else:
                    sub_lower_bound = sub_result[1]
                    if sub_lower_bound < sub_min_lower_bound:
                        sub_min_lower_bound = sub_lower_bound

            if isinf(sub_min_ncoins):
                # Reaching here means all of the children of the current node
                # either return ``(True, -1)`` or ``(False, lower_bound)``
                if isinf(sub_min_lower_bound):
                    # This mean all search returns ``(True, -1)`` or there is
                    # no valid child nodes to search, which means that the
                    # current amount cannot be made up
                    dp_ncoins[current_amount] = -1
                    return (True, -1)
                else:
                    lower_bound = sub_min_lower_bound + 1
                    dp_lower_bound[current_amount] = lower_bound
                    return (False, lower_bound)
            else:
                # The minimal coin count is found.
                min_ncoins = sub_min_ncoins + 1
                dp_ncoins[current_amount] = min_ncoins
                return (True, min_ncoins)
                

        rv = calc_minimum_coins(amount)
        assert rv[0]
        return calc_minimum_coins(amount)[1]



# This is a DFS+DP solution, which is too slow to pass the Leetcode tests
# (well, I would consider this a problem of Leetcode)
class DPSolution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        assert amount >= 0
        if amount == 0:
            return 0
        if len(coins) == 0:
            return -1
        sorted_coins = sorted(coins)
        amount_to_ncoins = {x:1 for x in coins}
        
        def calc_minimum_coins(sub_amount):
            min_ncoins = amount_to_ncoins.get(sub_amount)
            if min_ncoins is not None:
                return min_ncoins
            min_ncoins = -1
            for x in sorted_coins:
                assert x != sub_amount
                if x > sub_amount:
                    break
                sub_ncoins = calc_minimum_coins(sub_amount - x)
                if sub_ncoins != -1:
                    ncoins = 1 + sub_ncoins
                    if min_ncoins == -1 or ncoins < min_ncoins:
                        min_ncoins = ncoins

            amount_to_ncoins[sub_amount] = min_ncoins
            return min_ncoins
        
        return calc_minimum_coins(amount)




if __name__ == "__main__":
    f = Solution().coinChange
    assert f([10], 10) == 1
    assert f([10, 5, 2], 10) == 1
    assert f([42, 25, 15, 2], 45) == 3


if __name__ == "__main__":
    assert Solution().coinChange([], 0) == 0
    assert Solution().coinChange([], 10) == -1
    assert Solution().coinChange([1, 2, 5], 11) == 3
    assert Solution().coinChange([2], 11) == -1
    assert Solution().coinChange([1, 25, 30, 50], 55) == 2
    print(Solution().coinChange([186, 419, 83, 408], 6249))
    print(DPSolution().coinChange([186, 419, 83, 408], 6249))
    print(Solution().coinChange([77,82,84,80,398,286,40,136,162], 9794))
    print(DPSolution().coinChange([77,82,84,80,398,286,40,136,162], 9794))
    s = Solution()
    s2 = DPSolution()
    s_copied = CopiedSolution()
    import timeit
    print(timeit.timeit('s.coinChange([77,82,84,80,398,286,40,136,162], 9794)', number=10, setup='from __main__ import s,s2,s_copied'))
    print(timeit.timeit('s2.coinChange([77,82,84,80,398,286,40,136,162], 9794)', number=10, setup='from __main__ import s,s2,s_copied'))
    print(timeit.timeit('s_copied.coinChange([77,82,84,80,398,286,40,136,162], 9794)', number=10, setup='from __main__ import s,s2,s_copied'))
    print()
    print(timeit.timeit('s.coinChange([71,440,63,321,461,310,467,456,361], 9298)', number=10, setup='from __main__ import s,s2,s_copied'))
    print(timeit.timeit('s2.coinChange([71,440,63,321,461,310,467,456,361], 9298)', number=10, setup='from __main__ import s,s2,s_copied'))
    print(timeit.timeit('s_copied.coinChange([71,440,63,321,461,310,467,456,361], 9298)', number=10, setup='from __main__ import s,s2,s_copied'))
    print()
    print(timeit.timeit('s.coinChange([399,313,460,317,401,173,116,17,121], 7335)', number=10, setup='from __main__ import s,s2,s_copied'))
    print(timeit.timeit('s2.coinChange([399,313,460,317,401,173,116,17,121], 7335)', number=10, setup='from __main__ import s,s2,s_copied'))
    print(timeit.timeit('s_copied.coinChange([399,313,460,317,401,173,116,17,121], 7335)', number=10, setup='from __main__ import s,s2,s_copied'))
    print()

    # import sys
    # sys.setrecursionlimit(10000)
    # p1 = 193
    # p2 = 5179
    # print(timeit.timeit('print(s.coinChange([p1, p2], p1*p2))', number=1, globals=globals()))
    # print(timeit.timeit('print(s2.coinChange([p1, p2], p1*p2))', number=1, globals=globals()))
