from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import shutil

def every_downloads_chrome(driver):
    if not driver.current_url.startswith("chrome://downloads"):
        driver.get("chrome://downloads/")
    return driver.execute_script("""
        var items = downloads.Manager.get().items_;
        if (items.every(e => e.state === "COMPLETE"))
            return items.map(e => e.fileUrl || e.file_url);
        """)


def wait_element(driver, selector, type, tempo=20):
    return WebDriverWait(driver, tempo).until(EC.visibility_of_element_located((type, selector)))


def do_element(driver, finder, type, func, args=''):
    try:
        elem = None
        if finder is not None:
            elem = wait_element(driver, finder, type)
        
        if func == 'script':
            if finder is not None:
                driver.execute_script(args, elem)
            else:
                driver.execute_script(args)
        elif func == 'send_keys':
            elem.send_keys(args)

        elif func == 'click':
            elem.click()
        elif func == 'clear':
            elem.clear()
        else:
            pass
    except Exception as e:
        print("Erro no do_element: {}, func: {}, args: {}".format(finder, func, args))
        print(str(e))
