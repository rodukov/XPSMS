<div align="center">
<p>
  <img alt="python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
  <img alt="selenium" src="https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white">
  <img alt="geckodriver" src="https://img.shields.io/badge/Geckodriver-FF7139?style=for-the-badge&logo=Firefox-Browser&logoColor=white">
  <img alt="chromium" src="https://img.shields.io/badge/Chromium-4285F4?style=for-the-badge&logo=GoogleChrome&logoColor=white">
</p>
</div>
<div align="center">
<p>
  <img alt="XPSMS" src="./src/assets/xpsms32x.png" width="420px"/>
  <img alt="DISCLAIMER" src="./src/assets/disclaimer.png" width="420px"/>
</p>
</div>

XPSMS uses automation of browser engines Selenium under Python control to send requests for password recovery/registration, as a result of which the Target receives SMS messages or phone calls.

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

<h2> Active phone calls services <img alt="XPSMS" src="./src/assets/phonecall.png" width="22px"/> </h2>
<div align="left">
<p>
  <img alt="XPSMS" src="./src/assets/phonecallsbadge.png" width="420px"/>
</p>
</div>

| Service | Label | URL |
| ------- | ----- | --- |
| VK | <div align="center"><img src="https://img.shields.io/badge/vk-%23000000.svg?style=for-the-badge&logo=vk&logoColor=white"></div> | https://vk.com/ |
| Ozon | <div align="center"><img src="https://img.shields.io/badge/ozon-%23000000.svg?&style=for-the-badge&logo=ozon&logoColor=white"></div> | https://ozon.ru/ |

<h2> Active SMS services <img alt="XPSMS" src="./src/assets/smsreceive.png" width="22px"/> </h2>
<div align="left">
<p>
  <img alt="XPSMS" src="./src/assets/smsreceivebadge.png" width="420px"/>
</p>
</div>

| Service | Label | URL |
| ------- | ----- | --- |
| Viber | <div align="center"><img src="https://img.shields.io/badge/viber-%23000000.svg?style=for-the-badge&logo=viber&logoColor=white"></div> | https://www.viber.com/en/ |
| Yandex | <div align="center"><img src="https://img.shields.io/badge/Yandex-%23000000.svg?&style=for-the-badge&logo=yandex&logoColor=white"></div> | https://yandex.com/ |
| OK | <div align="center"><img src="https://img.shields.io/badge/odnoklassniki-%23000000.svg?&style=for-the-badge&logo=ok&logoColor=white"></div> | https://ok.ru/ |
| Wildberries | <div align="center"><img src="https://img.shields.io/badge/wildberries-%23000000.svg?&style=for-the-badge&logo=wildberries-&logoColor=white"></div> | https://www.wildberries.ru/ |

<h2> XPSMS Advanced Documentation <img alt="XPSMS" src="./src/assets/control.png" width="22px"/> </h2>
<div align="left">
<p>
  <img alt="XPSMS" src="./src/assets/docsbadge.png" width="420px"/>
</p>
</div>

### Architecture

| PATH | Description |
| ------- | ----- |
| `xpsms.py` | Main startup file |
| `requiremets.txt` | PIP dependency setup file |
| `README.md` | Main documentation file in English |
| `LICENSE` | File with license terms <b> GPL-3.0 license </b> 
| `.gitignore` | List of files that will not be used in git |
| `chromedriver.exe` | Not used. Chromium driver windows binary file |
| `src/assets/*` | Pictures for `README.md` |
| `src/services/*` | Control files for the driver. Each file name corresponds to its own service. |



