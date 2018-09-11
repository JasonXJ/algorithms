import statistics
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution:
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        candidates = wordlist[:]

        def similarity(w1, w2):
            return sum(1 for x, y in zip(w1, w2) if x == y)

        remaining_guesses = 10
        while remaining_guesses > 0 and len(candidates) > remaining_guesses:
            best_case = (len(candidates) + 1, len(candidates) + 1)
            best_word = wordlist[0]
            for w in wordlist:
                partitions = [0]*7
                for c in candidates:
                    partitions[similarity(w, c)] += 1
                case = (max(partitions), statistics.mean(partitions))
                if case < best_case:
                    best_case = case
                    best_word = w
            g = master.guess(best_word)
            if g == 6:
                # print(f"guess {best_word} and succeed")
                return
            candidates = [c for c in candidates if similarity(best_word, c) == g]
            remaining_guesses -= 1
            # print(f"guess {best_word}. result={g}. candidates_size={len(candidates)}. remaining_guesses={remaining_guesses}. candidates={candidates}")

        if remaining_guesses > 0:
            for c in candidates:
                master.guess(c)
                # print(f"guess {c}")


class Master:
    def __init__(self, target, wordlist):
        assert target in wordlist
        self.target = target
        self.wordlist = wordlist

    def guess(self, word):
        if word not in self.wordlist:
            return -1
        return self.similarity(self.target, word)
        
    @staticmethod
    def similarity(w1, w2):
        assert len(w1) == len(w2) == 6
        return sum(1 for x, y in zip(w1, w2) if x == y)

    def test(self, s):
        s.findSecretWord(self.wordlist, self)


test_cases = [
    ("hbaczn", ["gaxckt","trlccr","jxwhkz","ycbfps","peayuf","yiejjw","ldzccp","nqsjoa","qrjasy","pcldos","acrtag","buyeia","ubmtpj","drtclz","zqderp","snywek","caoztp","ibpghw","evtkhl","bhpfla","ymqhxk","qkvipb","tvmued","rvbass","axeasm","qolsjg","roswcb","vdjgxx","bugbyv","zipjpc","tamszl","osdifo","dvxlxm","iwmyfb","wmnwhe","hslnop","nkrfwn","puvgve","rqsqpq","jwoswl","tittgf","evqsqe","aishiv","pmwovj","sorbte","hbaczn","coifed","hrctvp","vkytbw","dizcxz","arabol","uywurk","ppywdo","resfls","tmoliy","etriev","oanvlx","wcsnzy","loufkw","onnwcy","novblw","mtxgwe","rgrdbt","ckolob","kxnflb","phonmg","egcdab","cykndr","lkzobv","ifwmwp","jqmbib","mypnvf","lnrgnj","clijwa","kiioqr","syzebr","rqsmhg","sczjmz","hsdjfp","mjcgvm","ajotcx","olgnfv","mjyjxj","wzgbmg","lpcnbj","yjjlwn","blrogv","bdplzs","oxblph","twejel","rupapy","euwrrz","apiqzu","ydcroj","ldvzgq","zailgu","xgqpsr","wxdyho","alrplq","brklfk"]),
    ("cymplm",
     ["eykdft","gjeixr","eksbjm","mxqhpk","tjplhf","ejgdra","npkysm","jsrsid","cymplm","vegdgt","jnhdvb","jdhlzb","sgrghh","jvydne","laxvnm","xbcliw","emnfcw","pyzdnq","vzqbuk","gznrnn","robxqx","oadnrt","kzwyuf","ahlfab","zawvdf","edhumz","gkgiml","wqqtla","csamxn","bisxbn","zwxbql","euzpol","mckltw","bbnpsg","ynqeqw","uwvqcg","hegrnc","rrqhbp","tpfmlh","wfgfbe","tpvftd","phspjr","apbhwb","yjihwh","zgspss","pesnwj","dchpxq","axduwd","ropxqf","gahkbq","yxudiu","dsvwry","ecfkxn","hmgflc","fdaowp","hrixpl","czkgyp","mmqfao","qkkqnz","lkzaxu","cngmyn","nmckcy","alpcyy","plcmts","proitu","tpzbok","vixjqn","suwhab","dqqkxg","ynatlx","wmbjxe","hynjdf","xtcavp","avjjjj","fmclkd","ngxcal","neyvpq","cwcdhi","cfanhh","ruvdsa","pvzfyx","hmdmtx","pepbsy","tgpnql","zhuqlj","tdrsfx","xxxyle","zqwazc","hsukcb","aqtdvn","zxbxps","wziidg","tsuxvr","florrj","rpuorf","jzckev","qecnsc","rrjdyh","zjtdaw","dknezk"]),
]

if __name__ == "__main__":
    m = Master(*test_cases[1])
    m.test(Solution())
