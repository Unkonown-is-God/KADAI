import morph
from markov import Markov
from util import format_error
from collections import defaultdict
import os.path
class Dictionary:
    '''思考エンジンの辞書クラス

    クラス変数
    DICT_RANDOM -- ランダム辞書のファイルへのパス
    DICT_PATTERN -- パターン辞書のファイルへのパス

    プロパティ
    random -- ランダム辞書
    pattern -- パターン辞書'''

    DICT={'random':'dics/random.txt',
          'pattern':'dics/pattern.txt',
          'template':'dics/template.txt',
          'markov':'dics/markov.dat'}
    
    def __init__(self):
        Dictionary.touch_dics()
        #ファイルからリストを作る
        self._random=Dictionary.load_random(Dictionary.DICT['random'])
        self._pattern=Dictionary.load_pattern(Dictionary.DICT['pattern'])
        self._template=Dictionary.load_template(Dictionary.DICT['template'])
        self._markov=Dictionary.load_markov(Dictionary.DICT['markov'])
    @staticmethod
    def load_random(filename):
        try:
            with open (filename,'r',encoding='utf-8') as f:
                return [x for x in f.read().splitlines() if x]#リスト内表記で検索
        except IOError as e:
            print(format_error(e))
    @staticmethod
    def load_pattern(filename):
        try:
            with open(filename,'r',encoding='utf-8') as f:
                return [Dictionary.make_pattern(x) for x in f.read().splitlines() if x]
                #リスト型に辞書型のデータを入れる　そのままはつかえない
        except IOError as e:
            print(format_error(e))
            return []
    @staticmethod
    def load_template(filename):
        templates=defaultdict(lambda:[],{})
        try:
            with open(filename,'r',encoding='utf-8') as f:
                #_templateの初期値を[]に設定
                for line in f:
                    count,template=line.strip().split('\t')
                    #countには置き換え部分の数　templateはテンプレートの文字列
                    if count and template:
                        count = int(count)
                        templates[count].append(template)
        except IOError as e:
            print(format_error(e))
        return templates
    @staticmethod
    def load_markov(filename):
        markov=Markov()
        try:
            markov.load(filename)
        except IOError as e:
            print(format_error(e))
        return markov

    def study(self,text,parts):
        study_random(text)
        study_pattern(text,parts)
        study_template(parts)
        study_markov(parts)
    def study_random(self,text):
        if not text in self._random:
            self._random.append(text)
    def study_pattern(self,text,parts):
        for word,part in parts:
            #parts = [(言葉,品詞)]
            #word=言葉,part=品詞
            if morph.is_keyword(part):
                duplicated = next((p for p in self._pattern if p['pattern'] == word), None)
                #リストを順次読み込み
                #duplicated wordがパターンと一致すればそのパターン辞書を代入
                if duplicated:
                    #もし入力されたテキストが応答パターンの中になかったら
                    if not text in duplicated['phrases']:
                        duplicated['phrases'].append(text)
                #言葉（名詞）とテキストを結び付けてパターンファイルに保存
                else:
                    self._pattern.append({'pattern':word,'phrases':[text]})
    def study_template(self,parts):
        #名詞のみ%noun%に置き換えた文字列を_template追加
        template=''
        count=0
        for word,part in parts:
            #templateを作りだす
            if morph.is_keyword(part):
                #名詞なら
                word = '%noun%'
                count += 1
            template += word

        if count>0 and template not in self._template[count]:
            #templateがテンプレートtxtの中になかったら追加
            self._template[count].append(template)
    def study_markov(self,parts):
       self._markov.add_sentence(parts) 

    def save(self):
        #メモリ上の辞書をファイルに記録
        with open(Dictionary.DICT['random'],'w',encoding='utf-8') as f:
            f.write('\n'.join(self.random))
        with open(Dictionary.DICT['pattern'],'w',encoding='UTF-8') as f:
            f.write('\n'.join([Dictionary.pattern_to_line(p) for p in self._pattern]))
        with open(Dictionary.DICT['template'],'w',encoding='utf-8') as f:
            for count,templates in self._template.items():
                #item keyとvalueで分解
                for template in templates:
                    #リスト型で保存されていたtemplatesを解体
                    f.write('{}\t{}\n'.format(count,template))
        self._markov.save(Dictionary.DICT['markov'])
    @staticmethod
    def touch_dics():
        #辞書ファイルをなければつくる
        for dic in Dictionary.DICT.values():
            #values keyをぬいた辞書データの値を返す リスト型で
            if not os.path.exists(dic):
                #dic変数ないの文字列と一致するファイルがあるかどうか確認bool型で返す
                open(dic,'w').close
    @staticmethod#クラス内で使う
    def make_pattern(line):#staticにはselfはいらん
        pattern,phrases=line.split('\t')#tabで区切ったリスト型をアンパック代入
        if pattern and phrases:
            return {'pattern':pattern,'phrases':phrases.split('|')}#辞書型のデータを返す |で区切る
    @staticmethod
    def pattern_to_line(pattern):
        #パターン辞書を文字列に変換する
        return '{}\t{}'.format(pattern['pattern'],'|'.join(pattern['phrases']))
    @property
    def random(self):
        return self._random
    @property
    def pattern(self):
        return self._pattern
    @property
    def template(self):
        return self._template
    @property
    def markov(self):
        return self._markov
