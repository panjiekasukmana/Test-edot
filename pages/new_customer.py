from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CustomerRegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def tap_new_customer(self):
        new_customer_button = self.wait.until(
            EC.element_to_be_clickable((MobileBy.XPATH, '(//android.widget.ImageView[@resource-id="id.edot.ework:id/img_menu"])[5]'))
        )
        continue_button.click()

    def tap_registration(self):
        registration_button = self.wait.until(
            EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.TextView[@resource-id="id.edot.ework:id/tvRegister"]'))
        )
        continue_button.click()

    def enter_outlet_name(self, outlet_name):
        outlet_field = self.wait.until(
            EC.presence_of_all_elements_located((MobileBy.XPATH, '//android.widget.EditText[@resource-id="id.edot.ework:id/et_outlet_name"]'))
        )[0]
        outlet_field.send_keys(outlet_name)

    def enter_phone_number(self, phone_number):
        phone_field = self.driver.find_elements(MobileBy.XPATH, '//android.widget.EditText[@resource-id="id.edot.ework:id/et_outlet_phone"]')[1]
        phone_field.send_keys(phone_number)

    def enter_email(self, email):
        email_field = self.driver.find_elements(MobileBy.CLASS_NAME, '//android.widget.EditText[@resource-id="id.edot.ework:id/et_outlet_email"]')[2]
        email_field.send_keys(email)

    def enter_contact_person(self, contact_name):
        contact_field = self.driver.find_elements(MobileBy.CLASS_NAME, '//android.widget.EditText[@resource-id="id.edot.ework:id/et_contact_person"]')[3]
        contact_field.send_keys(contact_name)

    def select_channel_type(self, channel_name):
        channel_dropdown = self.wait.until(
            EC.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("id.edot.ework:id/et_channel")'))
        )
        channel_dropdown.click()
        self.wait.until(
            EC.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("Modern Trade (MT)")'))
        ).click()

    def select_customer_type(self, customer_type):
        customer_dropdown = self.wait.until(
            EC.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("id.edot.ework:id/et_outlet_type")'))
        )
        customer_dropdown.click()

        self.wait.until(
            EC.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("Semi Grosir")'))
        ).click()

    def select_pricelist(self, pricelist_name="Default"):
        pricelist_dropdown = self.wait.until(
            EC.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("id.edot.ework:id/et_pricelist")'))
        )
        pricelist_dropdown.click()

        self.wait.until(
            EC.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().resourceId("id.edot.ework:id/tvName")'))
        ).click()

    def tap_continue(self):
        continue_button = self.wait.until(
            EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.Button[@resource-id="id.edot.ework:id/button_text"]'))
        )
        continue_button.click()

    def select_address_type(self, address_type):
        address_type_dropdown = self.wait.until(
            EC.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("id.edot.ework:id/et_address_type")'))
        )
        address_type_dropdown.click()
        self.wait.until(
            EC.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("Delivery Address")'))
        ).click()

     def tap_use_my_current_location(self):
        use_location_btn = self.wait.until(
            EC.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.LinearLayout").instance(5)'))
        )
        use_location_btn.click()
    
    def enter_address(self, address_text):
        address_field = self.wait.until(
            EC.presence_of_element_located((MobileBy.CLASS_NAME, 'new UiSelector().resourceId("id.edot.ework:id/etAddress")'))
        )
        address_field.send_keys(address_text)

    def select_province(self, province_name):
        address_type_dropdown = self.wait.until(
            EC.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Choose Province")'))
        )
        address_type_dropdown.click()
        self.wait.until(
            EC.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("PAPUA")'))
        ).click()

    def select_city(self, city_name):
        address_type_dropdown = self.wait.until(
            EC.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Choose City")'))
        )
        address_type_dropdown.click()
        self.wait.until(
            EC.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("KOTA JAYAPURA")'))
        ).click()

    def select_district(self, district_name):
        address_type_dropdown = self.wait.until(
            EC.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Choose District")'))
        )
        address_type_dropdown.click()
        self.wait.until(
            EC.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("HERAM")'))
        ).click()
    def select_sub_district(self, sub_district_name):
        address_type_dropdown = self.wait.until(
            EC.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Choose Sub District")'))
        )
        address_type_dropdown.click()
        self.wait.until(
            EC.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("WAENA")'))
        ).click()

    def select_postal_code(self, postal_code):
       address_type_dropdown = self.wait.until(
            EC.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Choose Postal Code")'))
        )
        address_type_dropdown.click()
        self.wait.until(
            EC.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().resourceId("id.edot.ework:id/txt_name")'))
        ).click()
    
    def tap_continue(self):
        continue_button = self.wait.until(
            EC.element_to_be_clickable((MobileBy.XPATH, '//android.widget.Button[@resource-id="id.edot.ework:id/button_text" and @text="Continue"]'))
        )
        continue_button.click()

    def enter_ktp_number(self, ktp_number):
        ktp_input = self.wait.until(
            EC.presence_of_all_elements_located((MobileBy.XPATH, '//android.widget.EditText[@resource-id="id.edot.ework:id/etInput"]'))
        )[0]
        ktp_input.send_keys(ktp_number)

    def upload_ktp_file(self, image_path_on_device):
        upload_btn = self.wait.until(
            EC.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR,
            '//android.view.ViewGroup[@resource-id="id.edot.ework:id/container_upload_photos"]'))
        )
        upload_btn.click()
        self.wait.until(
            EC.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().resourceId("id.edot.ework:id/container_upload_photos")'))
        ).click()

    def tap_submit(self):
        submit_btn = self.wait.until(
            EC.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Submit")'))
        )
        submit_btn.click()
    
    def draw_signature(self):
        signature_area = self.wait.until(
        EC.presence_of_element_located((MobileBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("id.edot.ework:id/signature_view")'))  
        )

        bounds = signature_area.rect
        start_x = bounds['x'] + 10
        start_y = bounds['y'] + bounds['height'] // 2
        end_x = start_x + 200
        self.driver.swipe(start_x, start_y, end_x, start_y, 500)

    def tap_register(self):
        register_btn = self.wait.until(
            EC.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("id.edot.ework:id/button_text")'))
        )
        register_btn.click()

    def tap_popup(self):
        pop_yes_btn = self.wait.until(
            EC.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Yes")'))
        )
        pop_yes_btn.click()

  



