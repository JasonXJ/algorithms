class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        
        def base_form(string):
            if string == '':
                return ''
            a_ord = ord('a')
            distance = ord(string[0]) - a_ord
            new_string_lst = []
            for x in string:
                x_new_ord = ord(x) - distance
                if x_new_ord < a_ord:
                    x_new_ord += 26
                new_string_lst.append(chr(x_new_ord))
            return ''.join(new_string_lst)


        groups = {}
        for string in strings:
            groups.setdefault(base_form(string), []).append(string)

        return list(groups.values())
