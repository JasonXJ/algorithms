class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}
        for str_ in strs:
            sorted_str_ = ''.join(sorted(str_))
            try:
                groups[sorted_str_].append(str_)
            except KeyError:
                groups[sorted_str_] = [str_]
        for str_lst in groups.values():
            str_lst.sort()
        return list(groups.values())
