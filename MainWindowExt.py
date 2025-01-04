import random
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6 import QtWidgets

from MODULE2.Exercise33.MainWindow import Ui_MainWindow


class MainWindowExt(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Mảng gốc
        self.original_array = []

        # Kết nối các nút với các hàm xử lý
        self.pushButtonRandomArray.clicked.connect(self.generate_random_array)
        self.pushButtonSumofArray.clicked.connect(self.sum_of_array)
        self.pushButtonCountoddelement.clicked.connect(self.count_odd_elements)
        self.pushButtonSumofelement.clicked.connect(self.sum_of_odd_elements)
        self.pushButtonSortAscending.clicked.connect(self.sort_array_ascending)
        self.pushButtonSortDescending.clicked.connect(self.sort_array_descending)
        self.pushButtonFindsmallestelement.clicked.connect(self.find_smallest_element)
        self.pushButtonIncrementdoublevalue.clicked.connect(self.increment_double_value)

    def generate_random_array(self):
        """Tạo mảng ngẫu nhiên với 10 phần tử"""
        self.original_array = [random.randint(1, 100) for _ in range(10)]
        self.lineEditOriginialArray.setText(str(self.original_array))

    def sum_of_array(self):
        """Tính tổng tất cả các phần tử trong mảng"""
        result = sum(self.original_array)
        self.lineEditResult.setText(str(result))

    def count_odd_elements(self):
        """Đếm số lượng phần tử lẻ trong mảng"""
        odd_count = sum(1 for x in self.original_array if x % 2 != 0)
        self.lineEditResult.setText(str(odd_count))

    def sum_of_odd_elements(self):
        """Tính tổng các phần tử lẻ trong mảng"""
        odd_sum = sum(x for x in self.original_array if x % 2 != 0)
        self.lineEditResult.setText(str(odd_sum))

    def sort_array_ascending(self):
        """Sắp xếp mảng theo thứ tự tăng dần"""
        sorted_array = sorted(self.original_array)
        self.lineEditResult.setText(str(sorted_array))

    def sort_array_descending(self):
        """Sắp xếp mảng theo thứ tự giảm dần"""
        sorted_array = sorted(self.original_array, reverse=True)
        self.lineEditResult.setText(str(sorted_array))

    def find_smallest_element(self):
        """Tìm phần tử nhỏ nhất trong mảng"""
        smallest = min(self.original_array) if self.original_array else None
        self.lineEditResult.setText(str(smallest))

    def increment_double_value(self):
        """Tăng gấp đôi giá trị của tất cả các phần tử trong mảng"""
        self.original_array = [x * 2 for x in self.original_array]
        self.lineEditOriginialArray.setText(str(self.original_array))
