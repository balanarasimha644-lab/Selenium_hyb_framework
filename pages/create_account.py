from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.basepage import BasePage


class CreateAccount(BasePage):
    #------- locators ---------------
    ENTER_ACCOUNT_INFO =(By.XPATH,"//b[text()='Enter Account Information']")
    FIRST_NAME_INPUT =(By.ID,"first_name")
    LAST_NAME_INPUT =(By.ID,"last_name")

    ADDRESS_L1_INPUT =(By.ID,"address1")
    COUNTRY_DROP_INPUT = (By.XPATH,"//select[@id='country']/option[@value!='']")
    STATE_INPUT = (By.ID,"state")
    CITY_INPUT = (By.ID,"city")
    ZIP_CODE_INPUT = (By.ID,"zipcode")
    MOBILE_NUMBER_INPUT = (By.ID,"mobile_number")
    CREATE_ACC_BUTTON = (By.XPATH,"//button[text()='Create Account']")

    #--------- constructor ----------
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    # -----Action methods -------
            

    def enter_fname(self,fname):
        self.enter_text(self.FIRST_NAME_INPUT,fname)    

    def enter_lname(self,lname):
        self.enter_text(self.LAST_NAME_INPUT,lname)          

    def enter_add_l1(self,address):
        self.enter_text(self.ADDRESS_L1_INPUT,address) 
           
    def select_country(self,address):
        self.select_by_text(self.COUNTRY_DROP_INPUT,address)

    def enter_state(self,st):
        self.enter_text(self.STATE_INPUT,st)  

    def enter_city(self,ct):
        self.enter_text(self.CITY_INPUT,ct)   

    def enter_zip(self,zipcd):
        self.enter_text(self.ZIP_CODE_INPUT,zipcd)    

    def enter_mobile_num(self,mob):
        self.enter_text(self.MOBILE_NUMBER_INPUT,mob)   
        