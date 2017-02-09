VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    words = text.upper().replace(',', ' ').replace('.', ' ').split()
    count = 0

    def check_for_stripes(word):
        if word[0] in VOWELS:
            for i in range(1, len(word)):
                if i % 2 == 0 and word[i] in VOWELS:
                    continue
                elif i % 2 == 1 and word[i] in CONSONANTS:
                    continue
                else:
                    return False
            return True
        else:
            for i in range(1, len(word)):
                if i % 2 == 0 and word[i] in CONSONANTS:
                    continue
                elif i % 2 == 1 and word[i] in VOWELS:
                    continue
                else:
                    return False
            return True

    for word in words:
        print(word)
        if not word.isalnum():
            word = word[:-1]
        if word.isalpha() and len(word) > 1:
            print('run checking...')
            if check_for_stripes(word):
                count += 1
    return count

# These "asserts" using only for self-checking and not necessary for auto-test
# if __name__ == '__main__':
#     assert checkio("My name is ...") == 3, "All words are striped"
#     assert checkio("Hello world") == 0, "No one"
#     assert checkio("A quantity of striped words.") == 1, "Only of"
#     assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"

print checkio('My,name,is Ksenia')