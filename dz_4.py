class WordsFinder:
    def __init__(self, *args):
        self.file_names = []
        for arg in args:
            self.file_names.append(arg)

    def get_all_words(self):
        all_words = {}
        pukt = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            word_list = []
            with open(file_name, encoding='utf-8') as file:
                for word in file:
                    for abc in word:
                        if abc in pukt:
                            word = word.replace(abc, '')
                    word_list += word.split()
                    all_words[file_name] = word_list
        return all_words

    def find(self, word):
        word = word.lower()
        finder = self.get_all_words()
        slov = {}
        for key, value in finder.items():
            len_value = len(value)
            for i in range(len_value):
                if value[i].lower() == word:
                    slov[key] = i + 1
                    return slov

    def count(self, word):
        word = word.lower()
        finder = self.get_all_words()
        slov = {}
        count = 0
        for key, value in finder.items():
            len_value = len(value)
            for i in range(len_value):
                if value[i].lower() == word:
                    count += 1
            slov[key] = count
            return slov


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('text'))
print(finder2.count('TEXT'))

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))
