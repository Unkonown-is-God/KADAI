class Responder:
     def __init__(self,name):#はじめに処理される
         self._name=name
     def response(self,text):#考え出された応答を返す
         return '{}ってなに?'.format(text)
     def name(self):#レスポンダーの名前
         return self._name
