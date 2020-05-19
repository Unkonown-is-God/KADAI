import os
import sys
from random import choice
from collections import defaultdict
import re
import copy
import dill
import morph

class Markov:
    #マルコフ連鎖による学習と生成
    '''クラス定数：
    ENDMARK　文章の終わりを表す記号
    CHAIN-MARK　連鎖の最大値'''
    ENDMARK = '%END'
    CHAIN-MAX=30

    def __init__(self):
        self._dic=defaultdict(lambda: defaultdict(lambda:[]))
        #マルコフ辞書 二次元配列のイメージ [key][key]=[value]
        self._starts=defaultdict(lambda:0)
        #文章が始まる単語の数
