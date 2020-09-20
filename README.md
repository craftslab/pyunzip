# pyunzip

[![PyPI](https://img.shields.io/pypi/v/pyunzip.svg?color=brightgreen)](https://pypi.org/project/pyunzip/)
[![Travis](https://travis-ci.com/craftslab/pyunzip.svg?branch=master)](https://travis-ci.com/craftslab/pyunzip)
[![Coverage](https://coveralls.io/repos/github/craftslab/pyunzip/badge.svg?branch=master)](https://coveralls.io/github/craftslab/pyunzip?branch=master)
[![License](https://img.shields.io/github/license/craftslab/pyunzip.svg?color=brightgreen)](https://github.com/craftslab/pyunzip/blob/master/LICENSE)



*pyunzip* is a streaming unzip utility written in Python.



## Requirement

- python (3.8+)
- pip



## Installation

### Ubuntu

```bash
apt update
apt install -y python3-dev python3-pip python3-setuptools
pip install pyunzip
```



### Windows

```
pip install -U pywin32
pip install -U pyinstaller
pip install -Ur requirements.txt

pyinstaller --clean --name pyunzip -F unzip.py
```



## Updating

```bash
pip install pyunzip --upgrade
```



## Running

```bash
TBD
```



## License

Project License can be found [here](https://github.com/craftslab/pyunzip/blob/master/LICENSE).



## Reference

- [ZIP specification](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT)
- [conflux](https://github.com/transcend-io/conflux)
- [node-unzip](https://github.com/EvanOxfeld/node-unzip)
- [python-zipstream](https://github.com/allanlei/python-zipstream)
- [sunzip](https://github.com/madler/sunzip)
- [zipstreamer](https://github.com/scosman/zipstreamer)
- [zipstream](https://github.com/krolaw/zipstream)
