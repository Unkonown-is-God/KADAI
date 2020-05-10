#coding: utf-8

'''
競技用問題でおきたりするエラーですね。無理に直す必要はないです。

下記のようにtry-except文を使いましょう。
'''

nyuryoku = []

try:
        while True:
                    s = input()
                            if s == '':
                                            break
                                                nyuryoku.append(s)

except EOFError:
        pass

    for s in nyuryoku:
            print(s)
