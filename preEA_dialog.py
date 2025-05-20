from qgis.PyQt.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QPushButton

class PreEADialog(QDialog):
    def __init__(self, iface):
        super().__init__()
        self.iface = iface
        self.setWindowTitle("PreEA Tool")
        
        layout = QVBoxLayout()
        
        # Population Layer Selector
        layout.addWidget(QLabel("Population Raster:"))
        self.population_combo = QComboBox()
        self.load_layers(self.population_combo, 'raster')
        layout.addWidget(self.population_combo)
        
        # Boundary Layer Selector
        layout.addWidget(QLabel("Boundary Layers:"))
        self.boundary_combo = QComboBox()
        self.load_layers(self.boundary_combo, 'vector')
        layout.addWidget(self.boundary_combo)
        
        # Run Button
        self.run_btn = QPushButton("Generate EAs")
        self.run_btn.clicked.connect(self.generate_eas)
        layout.addWidget(self.run_btn)
        
        self.setLayout(layout)

    def load_layers(self, combo, layer_type):
        combo.clear()
        for layer in QgsProject.instance().mapLayers().values():
            if (layer_type == 'raster' and layer.type() == layer.RasterLayer) or \
               (layer_type == 'vector' and layer.type() == layer.VectorLayer):
                combo.addItem(layer.name(), layer)

    def generate_eas(self):
        pop_layer = self.population_combo.currentData()
        boundary_layer = self.boundary_combo.currentData()
        
        if pop_layer and boundary_layer:
            # Call the algorithm here
            QMessageBox.information(self, "Success", "EA generation started!")
        else:
            QMessageBox.warning(self, "Error", "Please select all required layers")