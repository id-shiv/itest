from selenium import webdriver
import time

import pandas as pd
import numpy as np

# Insert source package path to import modules from config
import sys
src_path = sys.path[0].split('itest')[0] + 'itest/src'
print(f'inserting source path {src_path}')
sys.path.insert(0, src_path)
print(f'sys path after insert: {sys.path}')

from config import DRIVER_PATH

# constants
TAG_ATTRIBUTES = ['//*[@id]', '//*[@class]', '//*[@name]']
INPUT_TAGS = ['input', 'textarea', 'button']


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

def get_input_elements(url: str):
    driver = get_driver()
    driver = launch(URL, driver)

    input_elements = list()  # to contain all input elements

    for tag_type in TAG_ATTRIBUTES:
        # get only text from tag. e.g. id, class, name
        tag_type_text = tag_type.split('[')[1].split(']')[0][1:]

        # find all elements with specific tag type
        tags = driver.find_elements_by_xpath(tag_type)
        for tag in tags:
            if tag.tag_name in INPUT_TAGS:
                _input = dict()
                
                # collect all the input details, i.e. id, class, name and value
                _input['tag_id'] = tag.get_attribute('id')
                _input['tag_class'] = tag.get_attribute('class')
                _input['tag_name'] = tag.get_attribute('name')
                _input['tag_value'] = tag.get_attribute('value')
                _input['tag_type'] = tag.get_attribute('type')
                _input['tag_text'] = tag.text
                input_elements.append(_input)
    
    # filter only the unique tag details in the list
    input_elements = list(np.unique(np.array(input_elements).astype(str)))

    # close the browser
    driver.close()

    return input_elements

if __name__ == "__main__":
    # test above methods
    from config import URL
    
    # get input elements
    input_elements = get_input_elements(url=URL)
    for element in input_elements:
        print(element)
    