import sys
from PyQt6.QtWidgets import QApplication
from MainWindowExt import MainWindowExt


def main():
    # Tạo ứng dụng Qt
    app = QApplication(sys.argv)

    # Tạo cửa sổ chính từ MainWindowExt
    window = MainWindowExt()
    window.setWindowTitle("Interactive Array Software")
    window.show()

    # Bắt đầu vòng lặp sự kiện của Qt
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
