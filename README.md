<div align="center">
<p>
  <img alt="XPSMS" src="./src/assets/xpsms32x.png" width="600px"/>
</p>
</div>

### python xpsms.py `--help`
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

### fast examples for one Target
```python
python xpsms.py -p +7 -a +77777777777 --call --undetected
```
```python
python xpsms.py -p +7 -a +77777777777 --call --sms --undetected
```
```python
python xpsms.py -p +7 -a +77777777777 --sms
```
