import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException

import requests
import openai
import json

import textwrap
from IPython.display import display
from IPython.display import Markdown

import webbrowser

OPENAI_API_KEY = "YOUT_OPENAI_API_HERE"

service = Service(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
