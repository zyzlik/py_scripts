"""
words = ['friend', 'fred', 'and', 'friend', 'ted']
             0        1       2      3        4

lengt = 5
matrix 5*5
matrix = [['-', '', '', '', '']] # 0-0 (no-count) 0-1 0-2 0-3 0-4
"""


def find_word(message):
    words = message.lower().split(' ')
    for word in words:
        word.strip(',.:;')
    matrix = [[0 for i in range(len(words))] for j in range(len(words))]
    print(words)
    def first_letter(word1, word2):
        if word1[0] == word2[0]:
            return True
        return False

    def last_letter(word1, word2):
        if word1[-1] == word2[-1]:
            return True
        return False

    def len_compare(word1, word2):
        if len(word1) >= len(word2):
            ratio = len(word2) / len(word1) * 30
        else:
            ratio = len(word1) / len(word2) * 30
        return ratio

    def common_letters(word1, word2):
        uniq_letters = set(word1).union(set(word2))
        intersection = set(word1).intersection(set(word2))
        return (len(intersection) / len(uniq_letters) * 50)

    max_median = (0, None)
    for i in range(len(words)):
        for j in range(len(words)):
            if i == j:
                continue
            else:
                if first_letter(words[i], words[j]):
                    matrix[i][j] += 10

                if last_letter(words[i], words[j]):
                    matrix[i][j] += 10

                matrix[i][j] += len_compare(words[i], words[j])
                matrix[i][j] += common_letters(words[i], words[j])
        total = sum(matrix[i])
        median = total / (len(words) - 1)
        if median > max_median[0]:
            max_median = (median, words[i])

    return(max_median[1])


find_word('The Doors of Durin, Lord of Moria. Speak friend and enter. I Narvi made them. Celebrimbor of Hollin drew these signs')