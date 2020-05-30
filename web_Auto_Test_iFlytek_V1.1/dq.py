# 1. 准备--导包
# webdriver
from selenium import webdriver
import time

# 2. 打开浏览器--实例化一个浏览器驱动对象
# obj = 类名()
# Friefox()
# Chrome()
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
url = r"https://testbox.iflytek.com/"
driver.get(url)
driver.implicitly_wait(30)
time.sleep(2)

driver.add_cookie({'name':'anniversary_17801140346','value':'1'})
time.sleep(3)
driver.refresh()
time.sleep(3)
driver.quit()


# driver.find_element_by_class_name("login_icon").click()
# driver.find_element_by_id("account").click()
# driver.find_element_by_id("account").send_keys("13716957736")
# driver.find_element_by_id("password").click()
# driver.find_element_by_id("password").send_keys("yc111111")
# driver.find_element_by_id("loginrec").click()
# time.sleep(2)
#
# a = driver.find_element_by_xpath("//*[@id='menu_list']/li[2]/p")
#
# ActionChains(driver).move_to_element(a).perform()
# driver.find_element_by_link_text("中文机器快转").click()


# time.sleep(2)
# driver.quit()

