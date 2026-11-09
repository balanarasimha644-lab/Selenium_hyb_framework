import pytest
from pages.loginpage import Loginpage
from pages.create_account import CreateAccount
import time
from utilities.readproperties import ReadConfig
from utilities.logger import get_logger
import allure # type: ignore



logger = get_logger(__name__)
@allure.title("test_001 signup for new registration") 
def test_001_sign_up(Setup):
    try:
        with allure.step("Test Started"):
            logger.info("Test Started")
            logger.info("getting applications url")
            baseURL = ReadConfig.get_application_URl()
            logger.info("got  applications url")
        with allure.step("fixture setup method is called "):
            driver = Setup
            driver.get(baseURL)
            logger.info("Application url is entered")
            driver.maximize_window()
            logger.info("application url lanched and maximised the page")
            logger.info("diver given to login page")
            loginpage = Loginpage(driver)
            time.sleep(10)
        with allure.step("click signupfrom  buttton"):  
            loginpage.click_sigUpform()
            logger.info("clicked signup form button")
            loginpage.enter_user_name("simham")
            logger.info("user name entered")
            loginpage.enter_email_address("123aps@gmail.com")
            logger.info("email address entered")
        with allure.step("signup details enterd and click signup button"):      
            loginpage.click_signup()
            logger.info("clicked signup button")
            ac_reg = CreateAccount(driver)
            logger.info("driver changed to next page")
            ac_reg.wait_for_visibility(ac_reg.ENTER_ACCOUNT_INFO)

        with allure.step("account information screen is displayed"):    
            ac_reg.highlight_element(ac_reg.ENTER_ACCOUNT_INFO)
            logger.info("account information text is highlighted")
            result = ac_reg.get_text(ac_reg.ENTER_ACCOUNT_INFO)
            print(result)
            assert result == 'ENTER ACCOUNT INFORMATION', "Text invalid"
            logger.info("Assertion passed")

    except AssertionError as e :
        logger.error(f"Assertion failed: {e}")
 
        raise
    except Exception as e:
 
        logger.error(f"Test failed due to unexpected error: {e}")
 
        raise
