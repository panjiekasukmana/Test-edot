import pytest
from capabilities import create_driver

@pytest.fixture(scope="function")
def driver():
    driver = create_driver()
    yield driver
    driver.quit()
