class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        letter_to_word = {}
        seen_words = set()
        words = str.split()
        if len(pattern) != len(words):
            return False
        for letter, word in zip(pattern, words):
            expected_word = letter_to_word.get(letter)
            if expected_word is not None and word != expected_word:
                return False
            if expected_word is None:
                if word in seen_words:
                    return False
                seen_words.add(word)
                letter_to_word[letter] = word

        return True
