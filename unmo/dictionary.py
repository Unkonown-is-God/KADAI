class Dictionary:
    '''思考エンジンの辞書クラス

    クラス変数
    DICT_RANDOM -- ランダム辞書のファイルへのパス
    DICT_PATTERN -- パターン辞書のファイルへのパス

    プロパティ
    random -- ランダム辞書
    pattern -- パターン辞書'''

    DICT_RANDOM='dicts/random.txt'
    DICT_PATTERN='dicts/pattern.txt'
    
    def study(self,text):
        #ユーザーの発言をメモリに記録
        if not text in self._random:
            #もしnot(テキストとランダムリストが一致したとき)
            self._random.append(text)
    def save(self):
        #メモリ上の辞書をファイルに記録
        with open(Dictionary.DICT_RANDOM,'w',encoding='utf-8') as f:
            f.write('\n'.join(self.random))
    def __init__(self):
        #ファイルからリストを作る
        with open (Dictionary.DICT_RANDOM,'r',encoding='utf-8') as f:
            self._random=[x for x in f.read().splitlines() if x]#リスト内表記で検索
        with open(Dictionary.DICT_PATTERN,'r',encoding='utf-8') as f:
            self._pattern=[Dictionary.make_pattern(x) for x in f.read().splitlines() if x]
            #リスト型に辞書型のデータを入れる　そのままはつかえない
    @staticmethod#クラス内で使う
    def make_pattern(line):#staticにはselfはいらん
        pattern,phrases=line.split('\t')#tabで区切ったリスト型をアンパック代入
        if pattern and phrases:
            return {'pattern':pattern,'phrases':phrases.split('|')}#辞書型のデータを返す |で区切る
    @property
    def random(self):
        return self._random
    @property
    def pattern(self):
        return self._pattern
