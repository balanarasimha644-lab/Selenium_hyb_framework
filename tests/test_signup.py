import pytest
import os
from pages.loginpage import Loginpage
from pages.create_account import CreateAccount
from pages.signup_page import SignupPage
import time
from utilities.readproperties import ReadConfig
from utilities.logger import get_logger
from utilities.ExcelUtils import ExcelUtils
import allure # type: ignore

@allure.title("sign up using user name and password")
def test_tc_001_signup(Setup):
    baseURL = ReadConfig.get_application_URl()
    log = get_logger(__name__)
    path = os.path.abspath(os.curdir)+ "\\data\\testdata.xlsx"
    rows =ExcelUtils.getRowCount(path,"Sheet1")
    login_staus = []
    driver = Setup
    driver.get(baseURL)
    driver.maximize_window()
    sinuppage = SignupPage(driver)
    sinuppage.click_sigUpform()
    for item in range(rows +1):
        email = ExcelUtils.readData(path, "Sheet1" r, 1)
        password = ExcelUtils.readData(path, "Sheet1" r, 2)
        exp = ExcelUtils.readData(path, "Sheet1" r, 3)
        sinuppage.enter_user_email(email)
        sinuppage.enter_password(password)
        sinuppage.click_login()

        if exp == "pass":
           login_staus.append("login passed")
        elif exp =="fail":
            login_staus.append("login passed")
    driver.close()
    if "fail" not in login_staus:
        assert True
    else: 
        assert False
    log.info("data driven testing completed")      
