import unittest
import HtmlTestRunner
from selenium import webdriver

import os
import sys
import inspect
# fetch path to the directory in which current file is, from the root directory or C:\ (or whatever driver number it is)
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# extract the path to parent directory
parentdir = os.path.dirname(currentdir)
# insert path to the folder from parent directory from which the python module/file to be imported
sys.path.insert(0, parentdir)


from Resources.Locators import Locators
from Resources.TestData import TestData
from Resources.PO import Page
from Page import HomePage, LoginPage, AcknowledgementPage, NetworkMapPage, GeneratingGraphPage