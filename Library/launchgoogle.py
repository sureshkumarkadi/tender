#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     12-08-2017
# Copyright:   (c) suresh.kumar 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from selenium import webdriver
import time

browser = webdriver.Firefox(executable_path=r'C:\tender\FFDriver\geckodriver.exe')

time.sleep(2)

browser.get('https://www.google.co.in/')

time.sleep(2)

browser.title == 'Google'

print browser.title


browser.close()

