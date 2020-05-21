import re
from janome.tokenizer import Tokenizer
TOKENNIZER=Tokenizer()
def analyze(text):
    #textを形態素解析し[(surface,parts)]の形にして返す リスト型
    #表層系、品詞
    return [(t.surface,t.part_of_speech) for t in TOKENNIZER.tokenize(text)]
def is_keyword(part):
    return bool(re.match(r'名詞,(一般|代名詞|固有名詞|サ変接続|形容動詞語幹)',part))

if __name__ == "__main__":
    print(analyze(input()))