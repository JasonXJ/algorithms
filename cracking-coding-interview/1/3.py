def is_permutation(str1, str2):
    return sorted(str1) == sorted(str2)

if __name__ == '__main__':
    print(is_permutation('', 'fgabdec') == False)
    print(is_permutation('abcdefg', 'fgabdec') == True)
    print(is_permutation('abcdefg', 'fgabdez') == False)
