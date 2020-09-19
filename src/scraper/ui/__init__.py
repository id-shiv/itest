from selenium import webdriver
import time

import pandas as pd
import numpy as np

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

    inputs = list()  # to contain all input elements

    tag_types = ['//*[@id]', '//*[@class]', '//*[@name]']
    for tag_type in tag_types:
        # get only text from tag. e.g. id, class, name
        tag_type_text = tag_type.split('[')[1].split(']')[0][1:]

        tags = driver.find_elements_by_xpath(tag_type)
        for tag in tags:
            if tag.tag_name in ['input', 'textarea', 'button']:
                _input = dict()
                # _input['tag_type'] = tag_type_text
                _input['tag_id'] = tag.get_attribute('id')
                _input['tag_class'] = tag.get_attribute('class')
                _input['tag_name'] = tag.get_attribute('name')
                _input['tag_text'] = tag.text
                inputs.append(_input)
    
    inputs=list(np.unique(np.array(inputs).astype(str)))

    for _input in inputs:
        print(_input)
    driver.close()