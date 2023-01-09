<div align="center">

# BingX API Connector Python
[![PYPI version][pypi-shield]][pypi-url]
[![Python version][python-shield]][python-url]
[![License: GPLv3][license-shield]][license-url]

</div>

## 📌 About The Project

This is a Python package for bingX API, aims to provide a simple and easy-to-use interface for developers to access bingX API.

## 📌 Installation

```bash
pip install bingX-connector     # install from pypi
pip install -U bingX-connector  # upgrade the package to the latest version
```
> Please always upgrade to the latest version to ensure the latest features and bug fixes


## 📌 Features

- [x] Standard Contract
- [ ] Standard Contract Web Socket
- [x] Spot
- [ ] Spot Web Socket
- [x] Perpetual v1
- [ ] Perpetual v1 Web Socket
- [x] Perpetual v2
- [ ] Perpetual v2 Web Socket

## 📌 Usage

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

> For More Information, please look at the [bingX API document](https://bingx-api.github.io/docs/)

## [📌 Report a bug](https://github.com/Ming119/bingX-connector-python/issues)

- ### Please follow the below guidelines if you would like to report a bug:

  1. **Use the GitHub issue search** &mdash; check if the issue has already been reported.

  2. **Check if the issue has been fixed** &mdash; try to reproduce it using the latest `main` or development branch in the repository.

  3. **Isolate the problem** &mdash; create a [reduced test case](http://css-tricks.com/reduced-test-cases/) and a live example.


  Example:

  > Short and descriptive example bug report title
  >
  > A summary of the issue and the browser/OS environment in which it occurs. If
  > suitable, include the steps required to reproduce the bug.
  >
  > 1. This is the first step
  > 2. This is the second step
  > 3. Further steps, etc.
  >
  > `<url>` - a link to the reduced test case
  >
  > Any other information you want to share that is relevant to the issue being
  > reported. This might include the lines of code that you have identified as
  > causing the bug, and potential solutions (and your opinions on their
  > merits).

## [📌 Contribute](https://github.com/Ming119/bingX-connector-python/pulls)
-  ### Follow this process if you'd like your work considered for inclusion in the project
  1. [Fork](http://help.github.com/fork-a-repo/) the project, clone your fork, and configure the remotes:
  
      ```bash
      # Clone your fork of the repo into the current directory
      git clone https://github.com/<username>/bingX-connector-python.git
      # Navigate to the newly cloned directory
      cd bingX-connector-python
      # Assign the original repo to a remote called "upstream"
      git remote add upstream https://github.com/Ming119/bingX-connector-python
      ```

  2. If you cloned a while ago, get the latest changes from upstream:
  
      ```bash
      git checkout <dev-branch>
      git pull upstream <dev-branch>
      ```
  
  3. Create a new topic branch (off the main project development branch) to contain your feature, change, or fix:

      ```bash
      git checkout -b <topic-branch-name>
      ```

  4. Locally merge (or rebase) the upstream development branch into your topic branch:

      ```bash
      git pull [--rebase] upstream <dev-branch>
      ```

  5. Push your topic branch up to your fork:

      ```bash
      git push origin <topic-branch-name>
      ```
  6. [Open a Pull Request](https://help.github.com/articles/using-pull-requests/) with a clear title and description.

  >  **IMPORTANT**: By submitting a patch, you agree to allow us to license your work under the same license as that used by `bingX-connector-python`

[pypi-shield]: https://img.shields.io/pypi/v/bingX-connector
[pypi-url]: https://pypi.org/project/bingX-connector/
[python-shield]: https://img.shields.io/pypi/pyversions/bingX-connector
[python-url]: https://www.python.org/downloads/
[license-shield]: https://img.shields.io/github/license/Ming119/bingX-connector-python
[license-url]: https://www.gnu.org/licenses/gpl-3.0.en.html