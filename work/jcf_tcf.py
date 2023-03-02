import decimal
from decimal import Decimal
import work.random_number as rn
import logging
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QGuiApplication
from PyQt6.QtWidgets import QListView, QAbstractItemView, QMainWindow, QMessageBox

# 使用logging模块记录日志
logger = logging.getLogger("my_logger")


# 报价清单生成器
def quote_list_generator(pcs, kgs, cbm, location):
    # 获取一个ID数值
    id = rn.reandom()
    # 制作一个报价清单
    quote = f"""
    报价编号: {id} \n 
    件数: {pcs} ，重量: {kgs} ，体积: {cbm} \n
    地址: {location} \n
    """
    return quote


# 进仓价格计算
class jcf_price_calculator:
    def in_out(self, pcs, kgs, cbm, pallets, warehouse, overlarge):
        # 是洋山仓库
        if warehouse:
            # 是超大件
            if overlarge:
                # 体积价格 RMB 45/CBM(轻货价格)
                cbm_money = Decimal(cbm) * Decimal(80)
                # 重量价格 RMB 60/TON（重货价格）
                tone_money = Decimal(kgs) * Decimal(110)
                # 托盘价格 RMB 60/TON
                number_money = Decimal(pcs) * Decimal(110)
            # 不是超大件
            else:
                # 体积价格 RMB 45/CBM(轻货价格)
                cbm_money = Decimal(cbm) * Decimal(70)
                # 重量价格 RMB 60/TON（重货价格）
                tone_money = Decimal(kgs) * Decimal(100)
                # 托盘价格 RMB 60/TON
                number_money = Decimal(pcs) * Decimal(100)
        # 不是洋山仓库
        else:
            # 是超大件
            if overlarge:
                # 体积价格 RMB 45/CBM(轻货价格)
                cbm_money = Decimal(cbm) * Decimal(55)
                # 重量价格 RMB 60/TON（重货价格）
                tone_money = Decimal(kgs) * Decimal(70)
                # 托盘价格 RMB 60/TON
                number_money = Decimal(pcs) * Decimal(70)
            # 不是超大件
            else:
                # 体积价格 RMB 45/CBM(轻货价格)
                cbm_money = Decimal(cbm) * Decimal(45)
                # 重量价格 RMB 60/TON（重货价格）
                tone_money = Decimal(kgs) * Decimal(60)
                # 托盘价格 RMB 60/TON
                number_money = Decimal(pcs) * Decimal(60)
        # 总价格
        # 是否为托盘货物
        if pallets:
            money = Decimal.max(cbm_money, tone_money)
            money = Decimal.max(money, number_money)
            money = Decimal.max(money, 100)
        else:
            money = Decimal.max(cbm_money, tone_money)
            money = Decimal.max(money, 100)
        return str("{:.2f}".format(money))


class jcf:
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.fwbj.clicked.connect(self.fwbj)

    # 生成报价
    def fwbj(self):
        # 获取件数
        pcs = self.main_window.jianshu.text()
        # 获取重量
        kgs = self.main_window.zhongliang.text()
        # 获取体积
        cbm = self.main_window.tiji.text()
        # 检查是否是数字，不是数字将直接弹窗
        try:
            pcs_decimal = decimal.Decimal(pcs)
            kgs_decimal = decimal.Decimal(kgs)
            cbm_decimal = decimal.Decimal(cbm)
        except decimal.InvalidOperation:
            QMessageBox.warning(self.main_window, "警告", "必须是数字")
            return
        # 获取地址
        location = self.main_window.dizhi.text()
        # 生成报价清单
        quote = quote_list_generator(pcs, kgs, cbm, location)
        # 显示报价清单
        self.main_window.baojia_display.setText(quote)
        # 同时复制到剪贴板
        clipboard = QGuiApplication.clipboard()
        clipboard.setText(quote)
