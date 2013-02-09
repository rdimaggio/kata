from datetime import datetime
#import pdb; pdb.set_trace()


class WordCounter():

    def __init__(self):
        self.words = []
        self.sub_words = []
        self.word_counter = 0

    #@profile
    def load_dictionary(self, dictionary_file):
        # load the dictionary file
        f = open(dictionary_file, 'r')

        # loop through each word to load dictionary
        for line in f:
            #self.word_counter += 1
            formatted_line = line.lower().replace("\n", "")
            word_length = len(formatted_line)
            if word_length <= MAX_STRING_LENGTH:
                if word_length == MAX_STRING_LENGTH:
                    # create max character word list
                    self.words.append(formatted_line)
                elif word_length > MIN_STRING_LENGTH:
                    # create max character - 1 or less word list
                    self.sub_words.append(formatted_line)

        # convert sub word and word lists into sets
        self.dictionary = frozenset(self.sub_words)
        self.words_set = frozenset(self.words)

    #@profile
    def create_subword_list(self, max_string_length, min_string_length):
        self.combos = []
        # loop through max character word list
        for word in self.words_set:
            for x in range(max_string_length)[min_string_length:]:
                # check if beginning subword exists
                if word[:x] in self.dictionary:
                    # check if ending subword exists
                    if word[x:] in self.dictionary:
                        self.combos.append([word[:x], word[x:]])


if __name__ == '__main__':
    MAX_STRING_LENGTH = 6
    MIN_STRING_LENGTH = 1
    FILE = 'words.txt'

    start = datetime.now()
    wc = WordCounter()
    wc.load_dictionary(FILE)
    wc.create_subword_list(MAX_STRING_LENGTH, MIN_STRING_LENGTH)
    stop = datetime.now()

    print "dictionary word count: " + str(wc.word_counter)
    print "sub word count (between " + str(MAX_STRING_LENGTH - 1) + " and " + \
          str(MIN_STRING_LENGTH) + " letter words): " + \
          str(len(wc.sub_words))
    print "number of " + str(MAX_STRING_LENGTH) + " letter words: " + \
          str(len(wc.words_set))
    print "number of comb pairs: " + str(len(wc.combos))
    print "duration: " + str(stop - start)
    #print wc.combos
