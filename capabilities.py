from appium import webdriver

def create_driver():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",  # ganti jika pakai device fisik
        "appPackage": "com.edotapps.sfa",
        "appActivity": "com.edotapps.sfa.MainActivity",
        "automationName": "UiAutomator2",
        "autoGrantPermissions": True,
    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    driver.implicitly_wait(10)
    return driver
