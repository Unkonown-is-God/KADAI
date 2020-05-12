from random import choice #pythonにもとからあるランダムモジュールのチョイスだけインポーと
import re
class Responder:
     def __init__(self,name,dictionary):#はじめに処理される
         self._name=name
         self._dictionary=dictionary
     def response(self,*args):#入力を受け取って処理する予定
         pass
     @property
     def name(self):#レスポンダーの名前
         return self._name
class PatternResponder(Responder):
    #登録されたパターンに反応し応答
    def response(self,text):
        #パターンに合わせてフレーズを返す
        for ptn in self._dictionary.pattern:
            #unmoからdictionaryを持ってくる　そしてパターンの分だけ回す
            matcher = re.match(ptn['pattern'],text)
            #patternで登録されてるやつと入力された文字列を比較
            if matcher:
                chosen_response=choice(ptn['phrases'])
                return chosen_response.replace('%match%',matcher.group())
                #returnで終了されるからランダムは読み込まない
        return choice(self._dictionary.random)

class WhatResponder(Responder):#Responderを継承している
    def response(self,text):
        return '{}ってなに？'.format(text)#なにってきく
class RandomResponder(Responder):
    def response(self,_):
        #ユーザーから入力を受け取るよてい
        return choice(self._dictionary.random)
