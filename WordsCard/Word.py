class Word:

    def __init__(self, list_num, book_page, word_seq, eng_word, chn_word, starred):
        self.list_num = list_num
        self.book_page = book_page
        self.word_seq = word_seq
        self.eng_word = eng_word
        self.chn_word = chn_word
        self.lrn_times = 0
        self.err_times = 0
        self.starred = starred
