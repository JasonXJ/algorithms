class Solution(object):
    def getPermutation(self, n, k):
        from math import factorial
        sequence = []
        sorted_options = list(range(1, n+1))
        def build_sequence(k):
            if len(sorted_options) == 1:
                assert k == 1
                sequence.append(sorted_options[0])
                return
            else:
                fac = factorial(len(sorted_options)-1)
                for i in range(len(sorted_options)):
                    if i*fac < k <= (i+1)*fac:
                        sequence.append(sorted_options[i])
                        del sorted_options[i]
                        break
                else:
                    assert False
                build_sequence(k - i*fac)

        build_sequence(k)
        return ''.join(str(x) for x in sequence)

if __name__ == "__main__":
    print(Solution().getPermutation(3, 4))
