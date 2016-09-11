# DAG topological sort solution
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        char_nodes = {}

        # First create all the entries
        for word in words:
            for x in word:
                if x not in char_nodes:
                    char_nodes[x] = set()

        for i in range(1, len(words)):
            for x, y in zip(words[i-1], words[i]):
                if x != y:
                    char_nodes[y].add(x)
                    break
        
        # Topological sort
        NEW = 0
        VISITING = 1
        VISITED = 2
        char_node_status = {c:NEW for c in char_nodes}
        ordered_list = []
        def dfs(char):
            status = char_node_status[char]
            if status == VISITING:
                # Loop in graph
                return False
            elif status == VISITED:
                return True
            else:
                char_node_status[char] = VISITING
                for next_char in char_nodes[char]:
                    if not dfs(next_char):
                        return False
                char_node_status[char] = VISITED
                ordered_list.append(char)
            return True


        for char in char_nodes:
            if dfs(char) == False:
                return ''

        return ''.join(ordered_list)


def test():
    assert 'wertf' == Solution().alienOrder(["wrt", "wrf", "er", "ett", "rftt"])
    assert 'wertfx' == Solution().alienOrder(["xwrt", "xwrf", "xer", "xett", "xrftt"])
    assert Solution().alienOrder(["xywrt", "xywrf", "xyer", "xyett", "xyrftt"]) in ('wertfxy', 'wertfyx')
    assert Solution().alienOrder(["xwrty", "xwrf", "xer", "xett", "xrftt"]) in ('wertfxy', 'wertfyx')
    assert Solution().alienOrder(["ri","xz","qxf","jhsguaw","dztqrbwbm","dhdqfb","jdv","fcgfsilnb","ooby"]) == ''
