def find_word(message):
    words = message.lower().split(' ')
    coefs = {
        'first_letter': 10,
        'last_letter': 10,
        'length': 30,
        'common_letters': 50
    }

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
            return (float(len(word2)), len(word1))
        else:
            return (len(word1), len(word2))

    def common_letters(word1, word2):
        word1, word2 = word1, word2
        uniq_letters = set(word1).union(set(word2))
        intersection = set(word1).intersection(set(word2))
        return (float(len(intersection)), len(uniq_letters))

    max_median = ['', 0]
    for word1 in words:
        words_copy = words[:]
        words_copy.remove(word1)
        results = []
        for word2 in words_copy:
            coef = 0
            if first_letter(word1, word2):
                coef += coefs['first_letter']
            if last_letter(word1, word2):
                coef += coefs['last_letter']
            len_ratio = len_compare(word1, word2)
            coef += len_ratio[0] * coefs['length'] / len_ratio[1]
            letter_ratio = common_letters(word1, word2)
            coef += letter_ratio[0] * coefs['common_letters'] / letter_ratio[1]
            results.append(coef)
        median = sum(results) / len(results)
        if median >= max_median[1]:
            max_median[0] = word1
            max_median[1] = median
            print max_median

    return max_median[0]

print find_word("The Doors of Durin, Lord of Moria. Speak friend and enter. Narvi made them. Celebrimbor of Hollin drew these signs")
