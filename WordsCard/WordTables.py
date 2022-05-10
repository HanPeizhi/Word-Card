from .Word import *


class ListTables:
    """用来合表"""
    words_num = 0
    spend_time = 0

    def __init__(self, list_num):
        self._list_num          = list_num          # 单词手册上的Word List是几
        self._word_seq          = 0                 # 一共有几个单词，现在是第几个单词
        self._new_list          = []                # 新添加的单词表
        self._old_list          = []                # 原本本地保存的所有单词表
        self._total_list        = []                # 新的和旧的合起来一个表
        self._del_list          = []                # 原本本地删除掉的单词表
        self._del_new_words     = []                # 新添加的单词表中被删掉的单词列表
