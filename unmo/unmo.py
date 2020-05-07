from responder import Responder 
class Unmo:
    """人工無脳コアクラス。
    プロパティ:
    name -- 人工無脳コアの名前
    responder_name -- 現在の応答クラスの名前
    """

    def __init__(self, name):
        """文字列を受け取り、コアインスタンスの名前に設定する。
        ’What' Responderインスタンスを作成し、保持する。
        """
        self._name = name
        self._responder = Responder('What')

    def dialogue(self, text):
        """ユーザーからの入力を受け取り、Responderに処理させた結果を返す。"""
        return self._responder.response(text)

    @property
    def name(self):
        """unmoの名前"""
        return self._name

    @property
    def responder_name(self):
        """Responderの名前"""
        return self._responder.name

