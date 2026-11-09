from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.basepage import BasePage


class SignupPage(BasePage):
#------- locators ---------------
    SIGN_UP_OR_LOGIN_BUTTON =(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
    LOGIN_TO_ACCOUNT =(By.XPATH,"//div[@class='login-form']/child::h2[text()='Login to your account']")
    LOGIN_EMAIL_INPUT =(By.XPATH,"//input[@data-qa='login-email']")
    LOGIN_PASSWORD =(By.XPATH,"//input[@data-qa='login-password'] ")
    LOGIN_BUTTON =(By.XPATH,"//button[@data-qa='login-button']")
#------- constructor-----------------
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
#------- action methods-----------------
    def click_sigUpform(self):
        self.click(self.SIGN_UP_OR_LOGIN_BUTTON)
        
    def enter_user_email(self, email):
        self.enter_text(self.LOGIN_EMAIL_INPUT,email)
        

    def enter_password(self, password):
        self.enter_text(self.LOGIN_PASSWORD,password)
            

    def click_login(self):
        self.click(self.LOGIN_BUTTON)    
