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
import os
import time
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
print dir_path

folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))
print folder_path

sys.path.insert(0,folder_path+"\FFDriver")
sys.path.insert(0,folder_path+"\IEDriver")
sys.path.insert(0,folder_path+"\Library")

browser = webdriver.Firefox(executable_path=folder_path+'\FFDriver\geckodriver.exe')

time.sleep(2)

browser.get('https://www.google.co.in/')

time.sleep(2)

print"pass"

print"suresh"

browser.title == 'Google'

print browser.title


browser.close()

print"pass"
print"23102017now123"

