class Solution(object):
    def permuteUnique(self, nums):
        nums_count_dict = {}
        for x in nums:
            try:
                nums_count_dict[x] += 1
            except:
                nums_count_dict[x] = 1
        nums_counts = [[k, v] for k,v in nums_count_dict.items()]

        rv = []
        current = [None] * len(nums)
        def inner(nums_counts_length, current_length):
            if current_length == len(nums):
                rv.append(current[:])
                return
            for i in range(0, nums_counts_length):
                current_nums_count = nums_counts[i]
                current[current_length] = current_nums_count[0]
                current_nums_count[1] -= 1
                if current_nums_count[1] == 0:
                    # This number cannot be used, we need to "remove" it.
                    nums_counts[nums_counts_length - 1], nums_counts[i] = nums_counts[i], nums_counts[nums_counts_length - 1]
                    inner(nums_counts_length - 1, current_length + 1)
                    nums_counts[nums_counts_length - 1], nums_counts[i] = nums_counts[i], nums_counts[nums_counts_length - 1]
                else:
                    inner(nums_counts_length, current_length + 1)
                current_nums_count[1] += 1
        
        inner(len(nums_counts), 0)

        return rv

if __name__ == "__main__":
    permutations = Solution().permuteUnique([1,1,2,2,2,3])
    print(len(permutations))
    for p in permutations:
        print(p)
