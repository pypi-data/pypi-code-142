import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# CLICK_TYPE configures which key is used to open the post in a new tab
# CLICK_TYPE = Keys.COMMAND # Use this if you are on a Mac
CLICK_TYPE = Keys.CONTROL # Use this if you are on a PC

class Craigslist:
    def __init__(self):
        self.base_url = 'https://accounts.craigslist.org'
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def get_login_page(self):
        self.driver.get(f'{self.base_url}/login?rp=%2Flogin%2Fhome&rt=L')
    
    def login(self, username, password):
        email_box = self.driver.find_element(By.ID, 'inputEmailHandle')
        password_box = self.driver.find_element(By.ID, 'inputPassword')
        email_box.send_keys(username)
        password_box.send_keys(password)
        login_button = self.driver.find_element(By.CLASS_NAME, 'accountform-btn')
        login_button.click()
    
    def check_logged_in(self):
        try:
            self.driver.find_element(By.CLASS_NAME, 'submit-onetime-link-button')
            return False
        except:
            return True
            
    def filter_active_posts(self):
        active_button = self.driver.find_element(By.NAME, "filter_active")
        active_button.click()

    def set_home_window(self):
        self.home_window = self.driver.current_window_handle

    def get_posts(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "tr[class^='posting-row']")
    
    def get_post_date(self, post):
        return post.find_element(By.TAG_NAME, "time").text

    def command_click(self, element):
        ActionChains(self.driver) \
            .key_down(CLICK_TYPE) \
            .click(element) \
            .key_up(CLICK_TYPE) \
            .perform()
    
    def delete_post(self, post):
        delete_button = post.find_element(
            By.CSS_SELECTOR, "form[class^='manage delete']")
        self.command_click(delete_button)

    def contains_button_click(self, type, class_contains, value_contains):
        time.sleep(2)
        self.driver.find_element(
            By.XPATH, f"//{type}[contains(@class, '{class_contains}') and contains(@value, '{value_contains}')]").click()
        
    def repost(self, post):
        self.delete_post(post)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.contains_button_click('input', 'managebtn', 'Repost this Posting')
        self.contains_button_click('button', 'submit-button', 'continue')
        try:
            self.contains_button_click('button', 'button', 'Continue')
        except:
            self.contains_button_click('button', 'continue', 'continue')
            self.driver.find_element(By.XPATH, "//*[@id='leafletForm']/button[1]").click()
            time.sleep(2)
            self.contains_button_click('button', 'button', 'Continue')

    def get_renewal_buttons(self):
        return self.driver.find_elements(By.XPATH, "//input[contains(@class, 'managebtn') and contains(@value, 'renew')]")
