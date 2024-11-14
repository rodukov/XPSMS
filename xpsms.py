from selenium import webdriver
from src.services import *

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c')
parser.add_argument('-a')

aim = parser.parse_args().a
code = parser.parse_args().c

driver = webdriver.Firefox()
