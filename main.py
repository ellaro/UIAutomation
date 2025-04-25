import random
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(ChromeDriverManager().install())

def check_site_loads(driver):
    driver.set_page_load_timeout(30)
    try:
        driver.get("https://www.total-luck.com/")
        print("Website loaded successfully.")
        return True
    except Exception as e:
        print("Website loading failed.")
        return False


def await_presence_click(driver, xpath, keys=None):
    presence = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    presence.click()
    if keys:
        presence.send_keys(keys)
        print(f"Entered {keys}.")


def await_find_click(driver, xpath, keys=None):
    element = driver.find_element(By.XPATH, xpath)
    element.click()
    if keys:
        element.send_keys(keys)
        print(f"Entered {keys}.")


def check_logo_play(driver):
    try:
        result = check_site_loads(driver)
        if not result:
            return

        await_presence_click(driver, '//*[@id="header-homepage-link"]')
        print("Clicked on the main banner.")

        await_find_click(driver, '//*[@id="ctl00_ContentPlaceHolderMain_homePageTemplate"]/div/div/div[8]/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div')
        print("Video is playing for 5 seconds.")
        time.sleep(5)

    except Exception as e:
        print("Website loading failed.")


def check_registration(driver):
    try:
        result = check_site_loads(driver)
        if not result:
            return

        await_presence_click(driver, '//*[@id="myAccountIconButton"]')
        print("click on the register button.")
        time.sleep(5)

        await_presence_click(driver, '/html/body/form/div[5]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[12]/div/a')
        print("click on the register button.")
        time.sleep(4)

        cur_email = f'ella.rosenberg{random.randint(0, 1000)}@gmail.com'
        await_find_click(driver, '/html/body/form/div[5]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[3]/input', cur_email)
        time.sleep(2)

        psw = 'Ella19971'
        await_find_click(driver, '/html/body/form/div[5]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[4]/div/div/input', psw)
        time.sleep(2)

        await_find_click(driver, '//*[@id="chkIsPrivacyPolicyAccepted"]')
        print('clicked the checkbox of terms of use.')
        time.sleep(2)

        await_find_click(driver,'/html/body/form/div[5]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[7]/a')
        print('clicked the sign up button at the end.')
        time.sleep(15)

        await_presence_click(driver, '//*[@id="userMenuIconButton"]')
        time.sleep(2)

        await_find_click(driver,'/html/body/form/div[4]/div/div[2]/div[2]/ul/li[2]/div[2]/ul/li[6]/a')
        print('clicked the logout button.')
        time.sleep(5)
    except Exception as e:
        print(e)
        print("Registration test failed.")


if __name__ == "__main__":

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    result = check_site_loads(driver)  # בודק אם האתר נטען בהצלחה
    if not result:
        print("Test failed: Website didn't load.")
    else:
        check_logo_play(driver)  # בודק אם הסרטון מופעל
        check_registration(driver)  # בודק את תהליך הרישום
        print('All tests have passed successfully.')

    driver.quit()  # סוגר את הדפדפן בסוף

