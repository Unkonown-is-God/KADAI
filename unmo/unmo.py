from random import choice
from responder import RandomResponder,WhatResponder,PatternResponder
from dictionary import Dictionary

class Unmo:
    """人工無脳コアクラス。
    プロパティ:
    name -- 人工無脳コアの名前
    responder_name -- 現在の応答クラスの名前
    """
    #名前の設定を行うクラスだよ

    def __init__(self, name):
        """文字列を受け取り、コアインスタンスの名前に複数設定する。"""
        self._dictionary = Dictionary()
        self._name = name#Unmoの名前を設定している
        self._responders = {'random':RandomResponder('Random',self._dictionary),#辞書型でクラスを登録
                            'what':WhatResponder('What',self._dictionary),
                            'pattern':PatternResponder('Pattern',self._dictionary),
                            }
        self._responder = self._responders['pattern']#登録されたクラスをここで指定して呼びだしている
                                                    #初期設定としてrandom
                                                    #呼び出されたクラスはインスタンス化される（要するに__init__が動く)
    def dialogue(self, text):
        """ユーザーからの入力を受け取り、Responderに処理させた結果を返す。"""
        chosen_key=choice(list(self._responders.keys()))#辞書型のdict_keysをlistでリスト型にして返している
                                                        #それをchoiceでランダムに返す
        self._responder=self._responders[chosen_key]#ランダムに選ばれた応答クラスをインスタンス化
        response = self._responder.response(text)
        self._dictionary.study(text)
        return response

    def save(self):
        #Dictionaryのsaveを持ってくる
        self._dictionary.save()

    @property
    def name(self):
        """unmoの名前を返す"""
        return self._name

    @property
    def responder_name(self):
        """Responderの名前を返す"""
        return self._responder.name
