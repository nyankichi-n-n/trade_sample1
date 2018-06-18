# coding=utf-8

"""
このモジュールでは MACD(Moving Average Convergence Divergence)を実装しています。
"""


class MovingAverageConvergenceDivergence:
    """
    MACD(Moving Average Convergence Divergence)のクラスです。
    """
    __count = 0
    __LOOP_CNT9 = 36  # MACD9のための定数(15秒間隔なので36)
    __LOOP_CNT12 = 48  # EMA12のための定数(15秒間隔なので48)
    __LOOP_CNT26 = 104  # EMA26のための定数(15秒間隔なので104)
    __MACD9 = []
    __SMA12 = []
    __SMA26 = []
    __EMA12 = []
    __EMA26 = []
    # ※α（平滑定数）＝2 /（ｎ+1）
    # A12AAA = 2 / (12.0000 + 1.0000)
    # A26AAA = 2 / (26.0000 + 1.0000)
    __A12AAA = 2 / (48.0000 + 1.0000)
    __A26AAA = 2 / (104.0000 + 1.0000)
    __SMA12_AVE = 0.0000
    __SMA26_AVE = 0.0000
    __MACD9_AVE = 0.0000
    __MACD = 0.0
    __MACD9_AVE_pre = 0.0000
    __MACD_pre = 0.0

    def __init__(self, cnt9=36, cnt12=48, cnt26=104):
        """
        MACD(Moving Average Convergence Divergence)の初期化
        :param cnt9: シグナル
        :param cnt12: 短期EMA
        :param cnt26: 長期EMA
        """
        self.__count = 0
        self.__LOOP_CNT9 = cnt9
        self.__LOOP_CNT12 = cnt12
        self.__LOOP_CNT26 = cnt26
        self.__A12AAA = 2 / (cnt12 + 1.0000)
        self.__A26AAA = 2 / (cnt26 + 1.0000)
        for var in range(0, self.__LOOP_CNT12):
            self.__SMA12.append(self.__SMA12_AVE)

        for var in range(0, self.__LOOP_CNT26):
            self.__SMA26.append(self.__SMA12_AVE)

        for var in range(0, self.__LOOP_CNT12):
            self.__EMA12.append(self.__SMA12_AVE)

        for var in range(0, self.__LOOP_CNT26):
            self.__EMA26.append(self.__SMA12_AVE)

        for var in range(0, self.__LOOP_CNT9):
            self.__MACD9.append(self.__SMA12_AVE)

    def add(self, price):
        """
        仮想通貨のカレントプライスを追加し、MACD,Signalを戻す
        :param price: カレントプライス
        :return: MACD, SIGNAL, 一つ前のMACD, 一つ前のSIGNAL
        """
        self.__count += 1
        if self.__count <= self.__LOOP_CNT26:
            for var in range(self.__LOOP_CNT12 - 1, 0, -1):
                self.__SMA12[var] = self.__SMA12[var - 1]

            for var in range(self.__LOOP_CNT26 - 1, 0, -1):
                self.__SMA26[var] = self.__SMA26[var - 1]

            self.__SMA12[0] = price
            self.__SMA26[0] = price

            sum12 = 0.0000
            sum26 = 0.0000

            for var in range(0, self.__LOOP_CNT12):
                sum12 += self.__SMA12[var]

            for var in range(0, self.__LOOP_CNT26):
                sum26 += self.__SMA26[var]

            self.__SMA12_AVE = sum12 / self.__LOOP_CNT12
            self.__SMA26_AVE = sum26 / self.__LOOP_CNT26

            return False, 0, 0, 0, 0
        else:
            self.__MACD_pre = self.__MACD
            self.__MACD9_AVE_pre = self.__MACD9_AVE
            
            # #######################EMAの算出#########################
            for var in range(self.__LOOP_CNT12 - 1, 0, -1):
                self.__EMA12[var] = self.__EMA12[var - 1]

            for var in range(self.__LOOP_CNT26 - 1, 0, -1):
                self.__EMA26[var] = self.__EMA26[var - 1]

            # EMA ＝ B + α( A - B )
            self.__SMA12_AVE = self.__SMA12_AVE + (self.__A12AAA * (price - self.__SMA12_AVE))  # EMA12
            self.__SMA26_AVE = self.__SMA26_AVE + (self.__A26AAA * (price - self.__SMA26_AVE))  # EMA26

            # print('__EMA12:', self.__SMA12_AVE)
            # print('__EMS26:', self.__SMA26_AVE)

            self.__EMA12[0] = self.__SMA12_AVE
            self.__EMA26[0] = self.__SMA26_AVE
            # #######################EMAの算出#########################

            # #######################MACDの算出########################
            self.__MACD = self.__SMA12_AVE - self.__SMA26_AVE  # MACD ＝ 基準線(EMA) － 相対線(EMA)

            for var in range(self.__LOOP_CNT9 - 1, 0, -1):
                self.__MACD9[var] = self.__MACD9[var - 1]

            self.__MACD9[0] = self.__MACD

            sum9 = 0.0000
            for var in range(0, self.__LOOP_CNT9):
                sum9 += self.__MACD9[var]

            self.__MACD9_AVE = sum9 / self.__LOOP_CNT9

            # print('__MACD:', self.__MACD)
            # print('__MACD9:', self.__MACD9_AVE)

            # #######################MACDの算出########################
            if self.__count == self.__LOOP_CNT26 + 1:
                return False, 0, 0, 0, 0
            else:
                return True, self.__MACD, self.__MACD9_AVE, self.__MACD_pre, self.__MACD9_AVE_pre
