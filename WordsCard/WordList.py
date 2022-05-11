from .Word import Word
import pandas as pd
import random


class WordList:
    """
    本类主要用来创建单词表
    创建WordList时需要一个Word List值作为参数来构建实例
    然后开始往这个实例里的单词表添加单词
    单词的详细信息由Word类创建
    """
    def __init__(self, list_num):
        self._list_num          = list_num          # 单词手册上的Word List是几
        self._word_seq          = 0                 # 一共有几个单词，现在是第几个单词
        self._list              = []                # 新添加的单词表
        self._del_words         = []                # 原本本地删除掉的单词表

    def add_word(self, book_page, eng_word, chn_word, starred):
        """添加一个新单词，并且加入单词表中"""
        # 记录当前新建的单词表的是第几个Word List
        list_num = self._list_num
        # 记录是当前list中的第几个单词
        word_seq = self._word_seq = self._word_seq + 1
        # 创造一个新词
        word = Word(list_num, book_page, word_seq, eng_word, chn_word, starred)
        # 添加一个新词
        self._list.append(word)

    def print_list(self):
        """打印列表中所有单词"""
        for i in range(self._word_seq):
            word = self._list[i]
            print(word.book_page, i, word.eng_word, word.chn_word, word.starred)

    def edit_word(self, num):
        """选择一个词修改"""
        if 0 <= num < self._word_seq:
            in_str = input("Input: ")
            # 根据空格将字符串分割
            in_str = in_str.split()
            if len(in_str) == 6:
                word = Word(in_str[0], in_str[1], in_str[2], in_str[3], in_str[4], in_str[5])
                self._list[num] = word
            else:
                print("Input Error")
        else:
            print("Input Error")

    def del_word(self, num):
        """选择一个词删除，或者删除所有词"""
        if 0 <= num < self._word_seq:
            # 删除某个单词前，先将这个单词保存到删除列表
            self._del_words.append(self._list[num])
            self._list.pop(num)
        elif num <= -1:
            # 清空整个列表前，先把整个列表保存到删除列表
            self._del_words.extend(self._list)
            self._list.clear()
        else:
            print("Input Error!")

    def save_list(self, file_name):
        """将单词通过数组的形式保存为Excel文件"""
        # Excel文件中的列名称
        col_name = ['Word List', 'Book Page', 'Word Number', 'English Word',
                    'Chinese Word', 'Learned Times', 'Error Times', 'Starred']
        # 将对象列表转换成二维数组
        tb = []
        # 将列表中的每隔单词单独处理
        for i in range(self._word_seq):
            word = self._list[i]
            # 先获得单词的属性和值，然后只保留值
            word_val = word.__dict__.values()
            # 将转化为列表然后保存进二维数组
            tb.append(list(word_val))

        # 保存为文件
        dt = pd.DataFrame(tb, columns=col_name)
        dt.to_excel(file_name, index=0)

    def review_word(self):
        dic = {}
        # 随机选出四个词在单词表中的索引
        quiz_words_seq = random.sample(range(self._word_seq), 4)
        # 从四个索引中随机选出一个作为题目和正确答案
        quiz_que_num = random.choice(quiz_words_seq)
        # 保存选出来的索引的选项索引
        quiz_ans_num = quiz_words_seq.index(quiz_que_num)
        # 作为题目
        quiz_eng_word = self._list[quiz_que_num].eng_word
        print("Multiple choice: ", quiz_eng_word)
        # 打印选项
        for i in quiz_words_seq:
            print("{}. {}".format(quiz_words_seq.index(i), self._list[i].chn_word))
        # 公布真确答案
        print("Answer is: ", quiz_ans_num)

    def quiz_chn(self):
        pass

    def quiz_eng(self):
        pass



