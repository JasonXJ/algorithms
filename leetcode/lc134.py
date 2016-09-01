class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        current_sum = 0
        lowest_sum = 0
        lowest_index = -1
        for i in range(len(gas)):
            current_sum += gas[i] 
            current_sum -= cost[i]
            if current_sum < lowest_sum:
                lowest_sum = current_sum
                lowest_index = i

        if current_sum >= 0:
            return lowest_index + 1
        return -1
