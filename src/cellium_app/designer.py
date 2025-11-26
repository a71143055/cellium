from PySide6 import QtWidgets, QtCore
from cellium_app.canvas import CircuitCanvas
from cellium_app.metacell import MetaCellManager

class DesignerWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cellium — 세포 기반 메타러닝 회로 설계")
        self.resize(1200, 800)

        self.canvas = CircuitCanvas()
        self.setCentralWidget(self.canvas)

        self.prop_panel = QtWidgets.QWidget()
        self.prop_layout = QtWidgets.QVBoxLayout(self.prop_panel)
        self.prop_layout.setContentsMargins(6,6,6,6)

        self.info_label = QtWidgets.QLabel("Properties")
        self.prop_layout.addWidget(self.info_label)

        self.sim_button = QtWidgets.QPushButton("Run Simulation")
        self.sim_button.clicked.connect(self.run_simulation)
        self.prop_layout.addWidget(self.sim_button)

        self.train_button = QtWidgets.QPushButton("Start Meta-Learning")
        self.train_button.clicked.connect(self.start_meta_learning)
        self.prop_layout.addWidget(self.train_button)

        dock = QtWidgets.QDockWidget("Inspector", self)
        dock.setWidget(self.prop_panel)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)

        self.metacell = MetaCellManager()

    def run_simulation(self):
        netlist = self.canvas.export_netlist()
        result = self.metacell.simulate(netlist)
        QtWidgets.QMessageBox.information(self, "Simulation Result", str(result))

    def start_meta_learning(self):
        self.train_button.setEnabled(False)
        QtWidgets.QApplication.processEvents()
        history = self.metacell.train_sample()
        QtWidgets.QMessageBox.information(self, "Training Finished", f"History: {history}")
        self.train_button.setEnabled(True)
