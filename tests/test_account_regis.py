import pytest
from pages.loginpage import Loginpage
from pages.create_account import CreateAccount
import time
from utilities.readproperties import ReadConfig


def test_001_account_registration(setup):
    baseUrl = ReadConfig.get_application_URl()
    driver = setup
    driver.get(baseUrl)
    driver.maximize_window()
