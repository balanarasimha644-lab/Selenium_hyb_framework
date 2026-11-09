import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class BasePage:
 
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
 

    def debug_element(self, locator):
        element = self.driver.find_element(*locator)
        print("Enabled:", element.is_enabled())
        print("Disabled attr:", element.get_attribute("disabled"))
        print("Class:", element.get_attribute("class"))

    def wait_for_presence(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))

    def wait_for_visibility(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
    
 
    def wait_for_clickable(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
    

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
    

    def highlight_element(self, locator):

        element = self.driver.find_element(*locator)
        self.driver.execute_script(
            "arguments[0].style.border='3px solid red';", element
        )
        return element
    
    def highlight_web_element(self, element):
        self.driver.execute_script(
            "arguments[0].style.border='3px solid deepskyblue';", element
        )    
        time.sleep(0.7)
        self.driver.execute_script(
            "arguments[0].style.border='';", element  
        )   

    
    def is_element_enabled(self, locator):
        element = self.driver.find_element(*locator)
        return element.is_enabled()
    
    def is_web_element_enabled(self, element):
        return element.is_enabled()
    
    def is_web_element_disabled(self, element):
        return not element.is_enabled()
    
    def is_element_disabled(self, locator):
        element = self.driver.find_element(*locator)
        return not element.is_enabled()
    
    
    def is_element_selected(self, locator):
        element = self.driver.find_element(*locator)
        return element.is_selected()
    
    def is_element_not_selected(self, locator):
        element = self.driver.find_element(*locator)
        return not element.is_selected()
    
    def click(self, locator):
        element = self.wait_for_clickable(locator)
        element.click()
        
     
    def is_element_clickable(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
            return True
        except:
            return False
        
    def is_element_not_clickable(self, locator):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
            return False  
        except:
            return True    


    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )   # scroll to the element and bring that element to center
        time.sleep(2)   # just to see scroll


    def scroll_to_web_element(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

    def get_text(self, locator):
        element = self.driver.find_element(*locator)
        return element.text
    
    def find_elements(self,locator):
        elements = self.driver.find_elements(*locator)
        return elements
    
    def is_element_disabled_by_class(self, locator):
        element = self.driver.find_element(*locator)
        classes = element.get_attribute("class")
        print(classes)
        return "cursor-not-allowed" in classes
    
    def is_element_disabled_by_class_content(self, element):
        classes = element.get_attribute("class")
        # print(classes)
        return "cursor-none" in classes
    
    def js_click(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)
    
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    #******************************************************
    #input-fileds
    #******************************************************
    def enter_text(self, locator, text):
        element = self.driver.find_element(*locator)
        time.sleep(1)
        element.click()
        element.send_keys(text)

    def enter_text_generic(self, locator, text):
        element = locator
        time.sleep(1)
        element.click()
        element.send_keys(text)    
    
    def clear_text(self, locator):
        element = self.driver.find_element(*locator)
        element.click()
        element.send_keys(Keys.CONTROL,"a")
        element.send_keys(Keys.BACKSPACE)

    def get_input_value(self, locator):
        element = self.driver.find_element(*locator)
        return element.get_attribute("value")
    #---geneic
    def get_input_value_generic(self, locator):
        elements = self.driver.find_elements(*locator)
        return [elements.get_attribute("value") for elements in elements]
    
    def get_placeholder(self, locator):
        element = self.driver.find_element(*locator)
        return element.get_attribute("placeholder") 

    #--------------------- drop downs ---------------

    def select_by_text(self,locator, text):
        element = Select(self.driver.find_elements(*locator))
        for pick in element:
            if pick.text == text:
                pick.click()
                break
