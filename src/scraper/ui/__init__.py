from selenium import webdriver
import time

# Insert source package path to import modules from config
import sys
sys.path.insert(0, sys.path[0].split('src')[0] + 'src')

from config import DRIVER_PATH

def get_driver(browser: str='chrome'):
    try:
        print(f'Retrieving driver for {browser} at path {DRIVER_PATH}')
        if browser == 'chrome':
            driver = webdriver.Chrome(DRIVER_PATH)
            driver.maximize_window()
            print(f'Successfully created the driver using {DRIVER_PATH}')
            return driver
        else:
            print(f'Failed to understand the browser {browser}')
            return None
    except Exception as e:
        print(e)
        print(f'Failed to get driver for {browser} at path {DRIVER_PATH}')
        return None

def launch(url: str, driver: webdriver):
    try:
        print(f'Launching {url}')
        driver.get(url)
        print(f'Successfully launched {url}')
        return driver
    except Exception as e:
        print(e)
        print(f'Failed to launch {url}')
        return None

if __name__ == "__main__":
    from config import URL
    driver = get_driver()
    launch(URL, driver)

    ids = driver.find_elements_by_xpath('//*[@id]')
    for ii in ids:
        if ii.tag_name in ['input', 'textarea', 'button']:
            print(ii.tag_name)  # tag name of id
            print(ii.get_attribute('id'))  # id name as string
            print(ii.text)  # id name as string
            print('###############')
            break
    driver.close()