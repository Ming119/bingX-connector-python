# BingX API Connector Python

[![GUN 3.0 License][license-shield]][license-url]

[license-shield]: https://img.shields.io/github/license/Ming119/bingX-connector-python
[license-url]: https://www.gnu.org/licenses/gpl-3.0.en.html

## Usage

### Standard Contract
```python
from bingX.standard import Standard

standard = Standard(api_key, api_secret)
```

### Spot
```python
from bingX.spot import Spot

spot = Spot(api_key, api_secret)
```

### Perpetual Swap
```python
from bingX.perpetual import Swap

swap = Swap(api_key, api_secret)
```
