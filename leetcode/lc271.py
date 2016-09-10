from io import StringIO

class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        string_io = StringIO()
        for string in strs:
            string_io.write(string.replace(',', ',,'))
            string_io.write(u', ')
        return string_io.getvalue()
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        rv = []
        last_start = 0
        i = 0
        last_is_comma = False
        while i < len(s):
            if last_is_comma:
                last_is_comma = False
                if s[i] == ' ':
                    rv.append(s[last_start:i-1].replace(',,', ','))
                    last_start = i + 1
            elif s[i] == ',':
                last_is_comma = True
            i += 1
        assert last_start == i == len(s)

        return rv
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

def test():
    codec = Codec()
    def subtest(strs):
        assert codec.decode(codec.encode(strs)) == strs

    subtest(['abcd','haha'])
    subtest([])
    subtest([''])
    subtest(['', ''])
    subtest(['', 'adf', ''])
    subtest(["","4 "])


if __name__ == "__main__":
    codec = Codec()
    s = codec.encode(["","4 "])
    print(repr(s))
    print(codec.decode(s))
