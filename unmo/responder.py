from random import choice #pythonにもとからあるランダムモジュールのチョイスだけインポーと
import re
import morph
from markov import Markov
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
    def response(self,text,parts):
        #パターンに合わせてフレーズを返す
        for ptn in self._dictionary.pattern:
            #unmoからdictionaryを持ってくる　そしてパターンの分だけ回す
            matcher = re.search(re.escape(ptn['pattern']),text)
            #patternで登録されてるやつと入力された文字列を比較
            if matcher:
                chosen_response=choice(ptn['phrases'])
                return chosen_response.replace('%match%',matcher.group())
                #returnで終了されるからランダムは読み込まない
        return choice(self._dictionary.random)

class WhatResponder(Responder):#Responderを継承している
    def response(self,text,parts):
        return '{}ってなに？'.format(text)#なにってきく
class RandomResponder(Responder):
    def response(self,_,parts):
        #ユーザーから入力を受け取るよてい
        return choice(self._dictionary.random)
class TemplateResponder(Responder):
    def response(self,_,parts):
        keywords=[word for word,part in parts if morph.is_keyword(part)]
        #名詞を記録
        count=len(keywords)
        #記録された名詞の数を代入
        if count > 0:
            #countが１以上の時
            if count in self._dictionary.template.keys():
                template=choice(self._dictionary.template[count])
                for keyword in keywords:
                    template=template.replace('%noun%',keyword,1)
                        #一個置換
                return template
        return choice(self._dictionary.random)
class MarkovResponder(Responder):
    def response(self,_,parts):
        keyword=next((w for w,p in parts if morph.is_keyword(p)))
        response = self._dictionary.markov.generate(keyword)
        return response if response else choice(self._dictionary.random)

