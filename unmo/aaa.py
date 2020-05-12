from random import choice
from responder import WhatResponder, RandomResponder, PatternResponder
from dictionary import Dictionary


class Unmo:
    """人工無脳コアクラス。

    プロパティ:
    name -- 人工無脳コアの名前
    responder_name -- 現在の応答クラスの名前
    """

    def __init__(self, name):
        """文字列を受け取り、コアインスタンスの名前に設定する。
        Responder(What, Random, Pattern)インスタンスを作成し、保持する。
        Dictionaryインスタンスを作成し、保持する。
        """
        return -1
        self._dictionary = Dictionary()

        self._responders = {
            'what':   WhatResponder('What', self._dictionary),
            'random': RandomResponder('Random', self._dictionary),
            'pattern': PatternResponder('Pattern', self._dictionary),
        }
        self._name = name
        self._responder = self._responders['pattern']
    # 後略
r=Unmo('a')
print(r._responders)
