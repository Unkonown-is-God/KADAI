import re
from janome.tokenizer import Tokenizer
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
    
    TOKENNIZWR=Tokenizer()#クラス変数
    def study(self,text):
        self.study_random(text)
        self.study_pattern(text,Dictionary.analyze(text))
    def study_random(self,text):
        if not text in self._random:
            self._random.append(text)
    def study_pattern(self,text,parts):
        for word,part in parts:
            if self.is_keyword(part):
                duplicated = next((p for p in self._pattern if p['pattern'] == word), None)
                if duplicated:
                    if not text in duplicated['phrases']:
                        duplicated['phrases'].append(text)
                else:
                    self._pattern.append({'pattern':word,'phrases':[text]})
    def save(self):
        #メモリ上の辞書をファイルに記録
        with open(Dictionary.DICT_RANDOM,'w',encoding='utf-8') as f:
            f.write('\n'.join(self.random))
        with open(Dictionary.DICT_PATTERN,'w',encoding='UTF-8') as f:
            f.write('\n'.join([Dictionary.pattern_to_line(p) for p in self._pattern]))
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
    @staticmethod
    def analyze(text):
        #textを形態素解析し[(surface,parts)]の形にして返す リスト型
        #表層系、品詞
        return [(t.surface,t.part_of_speech) for t in Dictionary.TOKENNIZWR.tokenize(text)]
    @staticmethod
    def pattern_to_line(pattern):
        #パターン辞書を文字列に変換する
        return '{}\t{}'.format(pattern['pattern'],'|'.join(pattern['phrases']))
    @staticmethod
    def is_keyword(part):
        return bool(re.match(r'名詞,(一般|代名詞|固有名詞|サ変接続|形容動詞語幹)',part))
    @property
    def random(self):
        return self._random
    @property
    def pattern(self):
        return self._pattern
