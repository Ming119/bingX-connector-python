# BingX API Connector Python

[![PYPI version][pypi-shield]][pypi-url]
[![Python version][python-shield]][python-url]
[![License: GPLv3][license-shield]][license-url]


## Installation

```shell
pip install bingX-connector
```

## Usage

### Standard Contract
```python
from bingX.standard import Standard

client = Standard(api_key, api_secret)
```

### Spot
```python
from bingX.spot import Spot

client = Spot(api_key, api_secret)
```

### Perpetual Swap
```python
from bingX.perpetual import Swap

client = Swap(api_key, api_secret)
```

[pypi-shield]: https://img.shields.io/pypi/v/bingX-connector
[pypi-url]: https://pypi.org/project/bingX-connector/
[python-shield]: https://img.shields.io/pypi/pyversions/bingX-connector
[python-url]: https://www.python.org/downloads/
[license-shield]: https://img.shields.io/github/license/Ming119/bingX-connector-python
[license-url]: https://www.gnu.org/licenses/gpl-3.0.en.html