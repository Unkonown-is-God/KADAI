class Responder:
    def __init__(self,name):#はじめに処理される
        self._name=name
    def response(self,text):#考え出された応答を返す
        return '{}ってなに?'.format(text)
    def name(self):#レスポンダーの名前
        return self._name
class Unmo:
    def __init__(self,name):#はじめに処理される
        self._name=name
        self._responder=Responder('what')
    def dialogue(self,text):#応答を表示する
        print(self._responder.response(text))
    @property
    def name(self):
        #unmoの名前
        return self._name
    @property
    def responde_name(self):
        #レスポンダーの名前
        return self._responder.name
muno=Unmo(input())
muno.dialogue(input())
