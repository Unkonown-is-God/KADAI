def format__error(error):
    #例外を受け取り、名前とメッセージの形式で返す
    return '{}:{}'.format(type(error).__name__,str(error))