from pages.login_page import LoginPage

def test_login_success(driver):
    login = LoginPage(driver)
    login.enter_company_id("5049209")
    login.enter_username("qatestsalesman")
    login.enter_password("it.QA2025")
    login.tap_sign_in()
    print("Login flow executed.")
