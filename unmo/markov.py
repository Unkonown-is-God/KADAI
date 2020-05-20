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
    CHAIN_MAX=30

    def __init__(self):
        self._dic=defaultdict(lambda: defaultdict(lambda:[]))
        #マルコフ辞書 二次元配列のイメージ [key][key]=[value]
        #こんな感じの構造　{key:{key:[value1,value2,value3]},{},{}}
        self._starts=defaultdict(lambda:0)
        #文章が始まる単語の数
        
    #学習
    def add_sentence(self,parts):
        #三語以上でないと学習しないようにする
        if len(parts)<3:
            return

        #呼びだし元をグチャグチャにしないためにコピー
        parts=copy.copy(parts)
        #pythonの　a=b は　*a=&bと同意義　aの値を変えるとbの値まで変更してしまう
        #変更したくないときはcopyをしよう！

        prefix1,prefix2=parts.pop(0),parts.pop(0)
        #文章の頭に単語を代入

        #下にメソッドが宣言されている
        self._add_start(prefix1)
        #始まりの単語を記録せし者

        for suffix,_ in parts:
            #品詞は使わないので_
            self._add_surffix(prefix1,prefix2,suffix)
            #下に宣言されている
            #辞書型の中のリスト型にどんどん追記していく

            prefix1,prefix2=prefix2,suffix
            #左側にずれていくイメージ prefix1はいなくなるのであった
        self._add_suffix(prefix1,prefix2,Markov.ENDMARK)
        #文章が閉じたことを明記する

    def _add_suffix(self,prefix1,prefix2,suffix):
        self._dic[prefix1][prefix2].append(suffix)

    def _add_start(self,prefix1):
        self._starts[prefix1]+=1
        #頻度もチェックできて便利

    #文章の生成
    def generate(self,keyword):
        #辞書が空だとnoneを返す
        if not self._dic:
            return None

        prefix1=keyword if self._dic[keyword] else choise(list(self._dic.keys()))
        #keyword が　辞書に登録されていれば次の単語を代入　登録されていなければランダムに代入

        prefix2=chice(list(self._dic[prefix1].keys()))
        #prefix2をランダムで代入

        words=[prefix1,prefix2]
        #生成される文章の依り代

        for _ in range(Markov.CHAIN_MAX):
            #CHAIN_MAXまでループ

            suffix = choice(self._dic[prefix1][prefix2])
            #wordsに追加するsuffixを更新

            if suffix == Markov.ENDMARK:
                #suffixがEND_MARKなら終了
                break
            words.append(suffix)
            #wordsリストにsuffixを追加
            prefix1,prefix2=prefix2,suffix
            #prefix1,2を更新

        return ''.join(words)
        #生成された文章を返す
