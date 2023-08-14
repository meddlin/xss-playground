from selenium import webdriver
from selenium.webdriver.common.by import By


def test_eight_components():
    driver = webdriver.Chrome()

    driver.get("http://localhost:3000")

    # title = driver.title
    # assert title == "Web form"

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.ID, value="input-field")
    submit_button = driver.find_element(by=By.ID, value="btn-click")

    text_box.send_keys("Selenium")
    submit_button.click()

    message = driver.find_element(by=By.ID, value="response-display")
    value = message.text
    assert value == "Selenium"

    driver.quit()
    print("value is...")
    print(value)



test_eight_components()