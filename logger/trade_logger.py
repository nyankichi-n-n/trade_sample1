# coding=utf-8
"""
トレードロガー(Ver 1.1)

"""

import codecs
import datetime
import csv


class TradeLogger:
    """
    トレードロガー
    """
    
    def __init__(self, file_path, coin_name='mona'):
        """
        Content:
          コンストラクタ
        Param:
          1. file_path:    ファイルパス
          2. coin_name:    コイン名
        """
        now = datetime.datetime.now()
        self.__file_path = file_path + now.strftime("%Y%m%d-%H%M%S") + ".csv"
        self.__message_title = True
        self.write(func='件名',
                   coin_asset=coin_name + '資産',
                   jpy_asset='JPY資産',
                   order_id='オーダーID',
                   trade='トレード',
                   price='指定価格',
                   size='指定数',
                   last_trade_price='最終トレード価格',
                   market_price='市場価格',
                   market_bid_price='買い気配',
                   market_ask_price='売り気配',
                   mean_line1='平均線1',
                   mean_line2='平均線2',
                   sigma2='標準偏差',
                   bid_amount='買取引量',
                   ask_amount='売取引量',
                   bid_depth_amount='板買い',
                   ask_depth_amount='板売り',
                   macd='MACD',
                   signal='シグナル',
                   msg='備考')
        self.__message_title = False
    
    def write(self,
              func='',
              coin_asset=0,
              jpy_asset=0,
              order_id='',
              trade='',
              price=0,
              size=0,
              last_trade_price=0,
              market_price=0,
              market_bid_price=0,
              market_ask_price=0,
              mean_line1=0,
              mean_line2=0,
              sigma2=0,
              bid_amount=0,
              ask_amount=0,
              bid_depth_amount=0,
              ask_depth_amount=0,
              macd=0,
              signal=0,
              msg=''):
        """
        Content:
          書き込みメソッド
        Param:
          1. func: 機能名
          2. coin_asset: コイン資産
          3. jpy_asset: JPY資産
          4. order_id: オーダーID
          5. trade: 申請(BUY,SELL,CANCEL)
          6. price: 申請価格
          7. size: 申請コイン数
          8. last_trade_price: 最終トレード価格 
          9. market_price: 市場価格
          10. market_bid_price: 買い気配
          11. market_ask_price; 売り気配
          12. mean_line1: 平均線1
          13. mean_line2: 平均線2
          14. sigma2: 標準偏差
          15. bid_amount: 買い取引量
          16. ask_amount: 売り取引量
          17. bid_depth_amount: 板買い
          18. ask_depth_amount: 板売り
          19. macd: MACD
          20. signal; SIGNAL
          21. msg: 備考
        """
        # ログファイル内容作成
        csvlist = []
        if self.__message_title:
            csvlist.append("日付")
            csvlist.append("日時")
        else:
            now = datetime.datetime.now()
            csvlist.append(now.strftime("%Y/%m/%d"))
            csvlist.append(now.strftime("%H:%M:%S"))
        csvlist.append(func)
        csvlist.append(coin_asset)
        csvlist.append(jpy_asset)
        csvlist.append(order_id)
        csvlist.append(trade)
        if price == 0:
            csvlist.append('')
        else:
            csvlist.append(price)
        if size == 0:
            csvlist.append('')
        else:
            csvlist.append(size)
        if last_trade_price == 0:
            csvlist.append('')
        else:
            csvlist.append(last_trade_price)        
        if market_price == 0:
            csvlist.append('')
        else:
            csvlist.append(market_price)
        if market_bid_price == 0:
            csvlist.append('')
        else:
            csvlist.append(market_bid_price)
        if market_ask_price == 0:
            csvlist.append('')
        else:
            csvlist.append(market_ask_price)
        if mean_line1 == 0:
            csvlist.append('')
        else:
            csvlist.append(mean_line1)
        if mean_line2 == 0:
            csvlist.append('')
        else:
            csvlist.append(mean_line2)
        if sigma2 == 0:
            csvlist.append('')
        else:
            csvlist.append(sigma2)
        csvlist.append(bid_amount)
        csvlist.append(ask_amount)
        csvlist.append(bid_depth_amount)
        csvlist.append(ask_depth_amount)
        csvlist.append(macd)
        csvlist.append(signal)
        csvlist.append(msg)
        
        # ログファイルに書き込む
        with codecs.open(self.__file_path, "a", "utf-8-sig") as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(csvlist)
        
        # 初期化
        func = ''
        coin_asset = 0
        jpy_asset = 0
        order_id = ''
        trade = ''
        price = 0
        size = 0
        last_trade_price=0
        market_price = 0
        market_bid_price = 0
        market_ask_price = 0
        mean_line1 = 0
        mean_line2 = 0
        sigma2 = 0
        bid_amount = 0
        ask_amount = 0
        bid_depth_amount = 0
        ask_depth_amount = 0
        macd = 0
        signal = 0
        msg = ''

