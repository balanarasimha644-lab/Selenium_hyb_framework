from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.basepage import BasePage


class Loginpage(BasePage):
#------- locators ---------------
    URL= "https://automationexercise.com/ "
    SIGN_UP_OR_LOGIN_BUTTON =(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
    #------- new user registration ----------------
    NEW_USER = (By.CSS_SELECTOR, 'div.signup-form')
    NAME_INPUT = (By.XPATH, "//input[@data-qa='signup-name']")
    EMAIL_ADD_INPUT = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_SUBMIT = (By.XPATH,"//button[@data-qa ='signup-button']")

    #------- User has already account signup ----------------
    LOGIN_TO_YOUR_ACC = (By.XPATH, "//div[@class='login-form']")
    LOGIN_EMAIL_INPUT =(By.XPATH,"//input[@data-qa='login-email']")
    LOGIN_PASSWORD = (By.XPATH,"//input[@data-qa='login-password']")
    LOGIN =(By.XPATH,"//button[@data-qa='login-button']")

#------- constructor-----------------
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
#------- action methods-----------------
    def click_sigUpform(self):
        self.click(self.SIGN_UP_OR_LOGIN_BUTTON)
    def enter_user_name(self, uname):
        self.enter_text(self.NAME_INPUT,uname)
        

    def enter_email_address(self, uemail):
        self.enter_text(self.EMAIL_ADD_INPUT,uemail)
            

    def click_signup(self):
        self.click(self.SIGNUP_SUBMIT)    
