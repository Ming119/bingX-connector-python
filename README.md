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

### Perpetual v1
```python
from bingX.perpetual.v1 import Perpetual

client = Perpetual(api_key, api_secret)
```

### Perpetual v2
```python
from bingX.perpetual.v2 import Perpetual

client = Perpetual(api_key, api_secret)
```

> Note that you can not import `Perpetual v1` and `Perpetual v2` at the same time

[pypi-shield]: https://img.shields.io/pypi/v/bingX-connector
[pypi-url]: https://pypi.org/project/bingX-connector/
[python-shield]: https://img.shields.io/pypi/pyversions/bingX-connector
[python-url]: https://www.python.org/downloads/
[license-shield]: https://img.shields.io/github/license/Ming119/bingX-connector-python
[license-url]: https://www.gnu.org/licenses/gpl-3.0.en.html