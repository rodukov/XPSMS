<div align="center">
<p>
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
  <img src="https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white">
  <img src="https://img.shields.io/badge/Geckodriver-FF7139?style=for-the-badge&logo=Firefox-Browser&logoColor=white">
  <img src="https://img.shields.io/badge/Chromium-4285F4?style=for-the-badge&logo=GoogleChrome&logoColor=white">
</p>
</div>
<div align="center">
<p>
  <img alt="XPSMS" src="./src/assets/xpsms32x.png" width="340px"/>
  <img alt="XPSMS" src="./src/assets/disclaimer.png" width="340px"/>
</p>
</div>

## Basic usage

### Installation
The software requires the latest version of Python, Selenium(geckodriver, undetected-chromedriver)
```
pip install -r requirements.txt
```

### `python xpsms.py --help`
```
Provide XPSMS with user data

options:
  -h, --help           show this help message and exit
  -p, --prefix PREFIX  Target's country code. Must start with +.
  -a, --aim AIM        Target's phone number. Must start with +.
  -c, --call           Set up flag if calls are required.
  -s, --sms            Set up flag if SMS are required.
  -u, --undetected     Runs a modified Chromium engine instead of default Geckodriver.
```

> [!IMPORTANT]  
> UC2 driver is better for requesting calls. However, Geckodriver is more focused on sending SMS messages.

### Examples for one Target
> [!WARNING]  
> <b>All automatic requests are not proxied.</b> Accordingly, it is recommended to have a new "clean" IP address for each new session, otherwise the service will be able to detect an automatic request.

```python
python xpsms.py -p +7 -a +77777777777 --call --undetected
```
```python
python xpsms.py -p +7 -a +77777777777 --call --sms --undetected
```
```python
python xpsms.py -p +7 -a +77777777777 --sms
```
