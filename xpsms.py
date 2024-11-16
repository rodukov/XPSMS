from selenium import webdriver
from seleniumbase import SB
from argparse import ArgumentParser
from time import sleep

from src.services import *


"""Getting user arguments"""
parser = ArgumentParser(description='Provide XPSMS with user data')
parser.add_argument('-p', '--prefix', help="Target's country code. Must start with +.")
parser.add_argument('-a', '--aim', help="Target's phone number. Must start with +.")
parser.add_argument('-c', '--call', action='store_true', help="Set up flag if calls are required.")
parser.add_argument('-s', '--sms', action='store_true', help="Set up flag if SMS are required.")
parser.add_argument('-u', '--undetected', action='store_true', help="Runs a modified Chromium engine instead of default Geckodriver.")
args = parser.parse_args()

"""Distribute user arguments into global variables"""
aim = args.aim
code = args.prefix
call = args.call
sms = args.sms
undetected = args.undetected

def inject(driver):
    """Runs all available services one by one"""
    if call:
        vk(driver, aim, code)
        try:
            ozon(driver, aim, code)
        except:
            ...
    if sms:
        viber(driver, aim, code)
        yandex(driver, aim, code)
        ok(driver, aim, code)
        wildberries(driver, aim, code)

def main():
    """Start the driver"""
    if undetected:
        with SB(uc=True) as driver:
            inject(driver)
            sleep(2.5)
    if not undetected:
        driver = webdriver.Firefox()
        inject(driver)
main()