# coding=utf-8

import codecs
import datetime
import sys
import traceback


class ErrorLogger:
    """
    自作ロガー
    """
    
    def __init__(self, file_path):
        """
        Content:
          コンストラクタ
        Param:
          1. file_path:    ファイルパス(最後は拡張子を含まないファイル名)
        """
        now = datetime.datetime.now()
        self.__file_path = file_path + now.strftime("%Y%m%d-%H%M%S") + ".log"
    
    def write(self):
        """
        Content:
        書き込みメソッド
        """
        # エラーの情報をsysモジュールから取得
        info = sys.exc_info()
        # tracebackモジュールのformat_tbメソッドで特定の書式に変換
        tb_info = traceback.format_tb(info[2])
        # ログファイル内容作成
        line_text = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S ")
        line_text += "Python Error.\n"
        for tbi in tb_info:
            line_text += tbi + '\n'
        line_text += str(info[1]) + '\n'
        
        # ログファイルに書き込む
        with codecs.open(self.__file_path, "a", "utf-8") as f:
            f.write(line_text)
