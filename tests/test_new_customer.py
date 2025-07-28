from pages.customer_registration_page import CustomerRegistrationPage

def test_register_new_customer(driver):
    reg = CustomerRegistrationPage(driver)

    reg.tap_new_customer()
    reg.tap_registration()
    reg.enter_outlet_name("Toko QA Automation")
    reg.enter_phone_number("81234567890")
    reg.enter_email("tokoqa@example.com")
    reg.enter_contact_person("Panji QA")
    reg.tap_continue()
    reg.select_address_type("Delivery Address")
    reg.tap_use_my_current_location()
    reg.enter_ktp_number("3273010101010001")
    reg.upload_ktp_file("ktp.jpg")  
    reg.tap_submit() 
    reg.draw_signature()
    reg.tap_register()
    reg.tap_popup()





    