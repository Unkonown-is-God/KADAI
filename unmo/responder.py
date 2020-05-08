from random import choice #pythonにもとからあるランダムモジュールのチョイスだけインポーと
class Responder:
     def __init__(self,name):#はじめに処理される
         self._name=name
     def response(self,*args):#入力を受け取って処理する予定
         pass
     @property
     def name(self):#レスポンダーの名前
         return self._name
class WhatResponder(Responder):#かっこのなかでResponderを呼び出しているよ
    def response(self,text):
        return '{}ってなに？'.format(text)#なにってきく
class RandomResponder(Responder):
    RESPONSES=['今日は寒いね','チョコ食べたい','昨日十円拾った']#レスポンスの内容 クラス変数だよ
    def __init__(self,name):
        self._name=name #ランダムの名前
    def response(self,_):
        #ユーザーから入力を受け取るよてい
        return choice(RandomResponder.RESPONSES)

