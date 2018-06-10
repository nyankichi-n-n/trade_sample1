# coding=utf-8

"""
このモジュールでは 単純移動平均(SMA)、ボリンジャーバンド(BB) を実装しています。
カレントの価格を加味しています。
"""

import numpy as np


class SimpleMovingAverageBollingerBand:
    """
    単純移動平均(SMA)、ボリンジャーバンド(BB)のクラスです。
    """
    __MAL1 = []
    __MAL2 = []
    __count = 0
    __avg1 = 0
    __avg2 = 0
    __sigma = 0
    __avg1_pre = 0
    __avg2_pre = 0
    __sigma_pre = 0
    
    def __init__(self, period1=12, period2=104):
        """
        移動平均線とボリンジャーバンド
        :param period1: 短期SMA
        :param period2: 長期SMA
        """
        self.__count = 0
        self.__period1 = period1
        self.__period2 = period2
        for var in range(0, self.__period1):
            self.__MAL1.append(0.00000)
        for var in range(0, self.__period2):
            self.__MAL2.append(0.00000)

    def add(self, price):
        """
        仮想通貨のカレントプライスを追加し、移動平均線、ボリンジャーバンドを戻す
        :param price: カレントプライス
        :return: 短期移動平均、長期移動平均、ボリンジャーバンド、一つ前の短期移動平均、一つ前の長期移動平均、一つ前のボリンジャーバンド
        """
        # self.__avg1 = np.average(self.__MAL1)
        # self.__avg2 = np.average(self.__MAL2)
        # self.__sigma = np.std(self.__MAL2, ddof=1)
        self.__count += 1
        for var in range(0, self.__period1 - 1):
            self.__MAL1[var] = self.__MAL1[var + 1]
        self.__MAL1[self.__period1 - 1] = price
        for var in range(0, self.__period2 - 1):
            self.__MAL2[var] = self.__MAL2[var + 1]
        self.__MAL2[self.__period2 - 1] = price

        if self.__count <= self.__period2 + 1:
            self.__avg1 = np.average(self.__MAL1)
            self.__avg2 = np.average(self.__MAL2)
            self.__sigma = np.std(self.__MAL2, ddof=1)
            return False, 0, 0, 0, 0, 0, 0
        else:
            self.__avg1_pre = self.__avg1
            self.__avg2_pre = self.__avg2
            self.__sigma_pre = self.__sigma
        
            self.__avg1 = np.average(self.__MAL1)
            self.__avg2 = np.average(self.__MAL2)
            self.__sigma = np.std(self.__MAL2, ddof=1)
            return True, self.__avg1, self.__avg2, self.__sigma, self.__avg1_pre, self.__avg2_pre, self.__sigma_pre


