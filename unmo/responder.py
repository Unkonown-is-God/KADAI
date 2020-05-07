class Responder:
     def __init__(self,name):#はじめに処理される
         self._name=name
     def response(self,text):#考え出された応答を返す
         return '{}ってなに?'.format(text)
     def name(self):#レスポンダーの名前
     """AIの応答を制御するクラス。
     プロパティ:
     name -- Responderオブジェクトの名前
     """

     def __init__(self, name):
         """文字列を受け取り、自身のnameに設定する。"""
         self._name = name

     def response(self, text):
         """ユーザーからの入力(text)を受け取り、AIの応答を生成して返す。"""
         return '{}ってなに？'.format(text)

     @property
     def name(self):
         """応答オブジェクトの名前"""
         return self._name
