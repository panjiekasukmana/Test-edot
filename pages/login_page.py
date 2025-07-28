class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, company_id, email, password):
        self.driver.find_element_by_xpath('//android.widget.EditText[@resource-id="id.edot.ework:id/tv_company_id"]').send_keys(company_id)
        self.driver.find_element_by_xpath('//android.widget.EditText[@resource-id="id.edot.ework:id/tv_username"]').send_keys(email)
        self.driver.find_element_by_xpath('//android.widget.EditText[@resource-id="id.edot.ework:id/tv_password"]').send_keys(password)
        self.driver.find_element_by_xpath('//android.widget.Button[@resource-id="id.edot.ework:id/button_text"]').click()

    def is_logged_in(self):
        return "dashboard" in self.driver.page_source.lower()

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_company_id(self, company_id):
        company_field = self.wait.until(
            EC.presence_of_all_elements_located((MobileBy.XPATH, '//android.widget.EditText[@resource-id="id.edot.ework:id/tv_company_id"]'))
        )[0]
        company_field.send_keys(company_id)

    def enter_username(self, username):
        username_field = self.driver.find_elements(MobileBy.XPATH, '//android.widget.EditText[@resource-id="id.edot.ework:id/tv_username"]')[1]
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_elements(MobileBy.XPATH, '//android.widget.EditText[@resource-id="id.edot.ework:id/tv_password"]')[2]
        password_field.send_keys(password)

    def tap_sign_in(self):
        sign_in_btn = self.wait.until(
            EC.element_to_be_clickable((MobileBy.CLASS_NAME, '//android.widget.Button[@resource-id="id.edot.ework:id/button_text"]'))
        )
        sign_in_btn.click()

