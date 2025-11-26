from PySide6 import QtWidgets, QtGui, QtCore

class CellItem(QtWidgets.QGraphicsItem):
    def __init__(self, x, y, w=60, h=36, color=QtGui.QColor("#2FAF6A")):
        super().__init__()
        self.rect = QtCore.QRectF(-w/2, -h/2, w, h)
        self.setPos(x, y)
        self.color = color
        self.setFlags(QtWidgets.QGraphicsItem.ItemIsMovable | QtWidgets.QGraphicsItem.ItemIsSelectable)

    def boundingRect(self):
        return self.rect.adjusted(-2, -2, 2, 2)

    def paint(self, painter, option, widget):
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        pen = QtGui.QPen(QtGui.QColor("#0B2545"))
        pen.setWidth(1.5)
        painter.setPen(pen)
        brush = QtGui.QBrush(self.color)
        painter.setBrush(brush)
        painter.drawRoundedRect(self.rect, self.rect.height()/2, self.rect.height()/2)
        if self.isSelected():
            sel_pen = QtGui.QPen(QtGui.QColor("#FFC857"))
            sel_pen.setWidth(2)
            painter.setPen(sel_pen)
            painter.drawRoundedRect(self.rect, self.rect.height()/2, self.rect.height()/2)

class CircuitCanvas(QtWidgets.QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setScene(QtWidgets.QGraphicsScene(self))
        self.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.SmoothPixmapTransform)
        self.setBackgroundBrush(QtGui.QColor("#f5f7fa"))
        self.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        for i in range(3):
            item = CellItem(100 + i*120, 150)
            self.scene().addItem(item)

    def export_netlist(self):
        items = [it for it in self.scene().items() if isinstance(it, CellItem)]
        netlist = []
        for idx, it in enumerate(items):
            netlist.append({
                "id": f"cell_{idx}",
                "x": it.pos().x(),
                "y": it.pos().y(),
                "w": it.rect.width(),
                "h": it.rect.height()
            })
        return netlist
