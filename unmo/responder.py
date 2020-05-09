from random import choice #pythonにもとからあるランダムモジュールのチョイスだけインポーと
class Responder:
     def __init__(self,name):#はじめに処理される
         self._name=name
     def response(self,*args):#入力を受け取って処理する予定
         pass
     @property
     def name(self):#レスポンダーの名前
         return self._name
class WhatResponder(Responder):#Responderを継承している
    def response(self,text):
        return '{}ってなに？'.format(text)#なにってきく
class RandomResponder(Responder):
    def __init__(self,name):#Responderの__init__をオーバーライド　親の__init__は自動的に呼び出されない
        super().__init__(name) #ランダムの名前 親の__init__を呼び出している
                               #__init__のnameを親に渡している
        self._responses=[]#からのリスト
        with open('dict/random.txt','r',encoding='utf-8') as f:
            #txtの文字コードはutf-8にして 読み込みモードで開いているよ withを使うと勝手に閉じてくれるよ　
            for line in f:#一行ずつfの内容を読み取りlineに渡される
                if line:#lineの中身が空じゃないとき
                    line=line.strip()#lineの空白や改行コードが消される
                    self._responses.append(line)#lineの中身が_responsesに追加される
    def response(self,_):
        #ユーザーから入力を受け取るよてい
        return choice(self._responses)

