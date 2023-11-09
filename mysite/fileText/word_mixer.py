import random

class WordMixer:
    def __init__(self, f):
        self.load_file(f)
        self.mix_words()

    def load_file(self, f):
        with open("fileText/words.txt", "wb+") as destination:
            for chunk in f.chunks():
                destination.write(chunk)

    def mix_words(self):
        with open("fileText/words.txt", 'r') as old_file:
            words_lines = old_file.readlines()
            with open("fileText/mixed-words.txt", 'w') as new_file:
                new_file.write('')
            for line in words_lines:
                new_words = []
                for word in line.split(' '):
                    if len(word) > 2:
                        word_center = list(word[1:-1])
                        random.shuffle(word_center)
                        new_words.append(word[0] + ''.join(word_center) + word[-1])
                    else:
                        new_words.append(word)
                with open("fileText/mixed-words.txt", 'a') as new_file:
                    new_file.writelines(' '.join(new_words))


