from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_xss():
    driver = webdriver.Chrome()

    driver.get("http://localhost:3000")

    # title = driver.title
    # assert title == "Web form"

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.ID, value="input-field")
    submit_button = driver.find_element(by=By.ID, value="btn-click")

    text_box.send_keys("<image/src/onerror=prompt(8)>")
    submit_button.click()


    # Xss should happen in here
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        print("alert is present")
        print('XSS attack is successful')
    except TimeoutException:
        print("No alert is present")


    # message = driver.find_element(by=By.ID, value="response-display")
    # value = message.text
    # assert value == "Selenium"

    driver.quit()
    # print("value is...")
    # print(value)



test_xss()