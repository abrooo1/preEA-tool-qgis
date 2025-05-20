from qgis.PyQt.QtWidgets import QAction, QMessageBox
from qgis.core import QgsProject
from .preEA_dialog import PreEADialog

class PreEATool:
    def __init__(self, iface):
        self.iface = iface
        self.dlg = None

    def initGui(self):
        self.action = QAction("PreEA Tool", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("Census Tools", self.action)

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        self.iface.removePluginMenu("Census Tools", self.action)

    def run(self):
        if not self.dlg:
            self.dlg = PreEADialog(self.iface)
        self.dlg.show()