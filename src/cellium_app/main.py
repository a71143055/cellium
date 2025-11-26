import sys
from PySide6 import QtWidgets, QtGui
from cellium_app.designer import DesignerWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("Cellium")
    try:
        app.setWindowIcon(QtGui.QIcon("assets/icon.ico"))
    except Exception:
        pass
    win = DesignerWindow()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
