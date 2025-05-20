# PreEA Tool for QGIS

![Plugin Icon](icon.png)

Automatically generates census enumeration areas from population and boundary data.

## Installation
1. Download [PreEA_Tool.zip](https://github.com/abrooo1/PreEA-Tool/releases)
2. In QGIS: `Plugins` → `Manage and Install Plugins` → `Install from ZIP`

## Usage
```python
# Sample code to generate EAs
from preEA_algorithm import generate_eas
eas = generate_eas(pop_layer, boundary_layer)
```

## License
MIT License - See [LICENSE](LICENSE)