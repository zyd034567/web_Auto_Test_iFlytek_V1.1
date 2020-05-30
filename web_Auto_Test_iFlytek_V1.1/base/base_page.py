import os
import time
from selenium.webdriver.support.wait import WebDriverWait
from utils import DriverUtil
import logging


# 对象库层-基类
class BasePage:

    def __init__(self):
        self.driver = DriverUtil.get_driver()

    # 定位元素
    def find_element(self, location, timeout=5.0, poll=1.0):
        logging.info("location={}".format(location))
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(location[0], location[1]))

    # 定位一组元素
    def find_elements(self, location,timeout=5.0, poll=1.0):
        logging.info("location={}".format(location))
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(location[0], location[1]))


# 操作层-基类
class BaseHandle:

    # 输入操作
    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)


class BaseAction(DriverUtil):
    def __init__(self):
        self.driver = DriverUtil.get_driver()
        self.base_page = BasePage()

    def exist_text(text):
        """
        判断页面中是否存在指定的文本内容
        :param text: 文本内容
        :return: True:存在; False:不存在
        """
        try:
            xpath = "//*[contains(text(), '{}')]".format(text)
            element = DriverUtil.get_driver().find_element_by_xpath(xpath)
            return element is not None
        except Exception as e:
            print("current page_tpshop not contains [{}]".format(text))
            logging.exception(e)
            return False

    def switch_new_window(self):

        """
        切换到新窗口
        """
        # 等待一下新窗口的打开
        time.sleep(3)
        # driver = DriverUtil.get_driver()
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def save_screenshot(self):
        """
        保存截图
        """
        file_path = os.getcwd() + '/Screenshots/'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logging.info("开始截图并保存")

        except Exception as e:
            logging.error("出现异常", format(e))

    def popup_window_handle(self, result="dismiss"):
        """
        弹出窗处理  1.alert 警告框 2. confirm 确认框  3. prompt 提示框
        """
        alert = self.driver.switch_to.alert  # 获取弹出框对象
        if result == "text":
            alert.text()       # 获取弹出框的提示内容
        elif result == "accept":
            alert.accept()     # 点击确定按钮，关闭弹出框
        elif result == "dismiss":
            alert.dismiss()    # 取消对话框选项
        else:
            raise Exception("请传入正确的参数 text/accept/dismiss/")

    def sliding_scroll_bar(self, js="js_down"):
        """
        滑动 滚动条    down: 从上往下    right: 从左往右

        """
        if js == "js_down":
            i = 100
            while i <= 2000:
                js_down = ("window.scrollTo(0,%d)" % i)# 操作滚动条向下滑动
                self.driver.execute_script(js_down)
                i += 100
                self.save_screenshot()
                time.sleep(1)

        elif js == "js_right":
            i = 100
            while i <= 2000:
                js_right = ("window.scrollTo(%d,0)" % i)  # 操作滚动条向右滑动
                self.driver.execute_script(js_right)
                time.sleep(1)
                i += 100
        else:
            raise Exception("请传入正确的参数js_down/js_right")




    #
    # def scroll_find_element(self, feature, js="js_down"):
    #     """
    #     边滑边找，如果找到则返回，如果没有找到则抛异常
    #     :param feature: 元素的特征
    #     :return: 元素
    #     """
    #     if js == "js_down":       # 操作滚动条向下滑动找元素
    #         i = 200
    #         while i <= 4000:
    #                 js_down = ("window.scrollTo(0,%d)" % i)
    #                 self.driver.execute_script(js_down)
    #                 time.sleep(1)
    #                 # self.home_proxy.entrance_about_us()
    #                 if self.driver.find_element(feature):
    #                     return self.driver.find_element(feature)
    #                 else:
    #                     print("没找到")
    #                 i += 200
    #
    #     elif js == "js_right":           # 操作滚动条向右滑动找元素
    #         i = 200
    #         while i <= 4000:
    #             js_right = ("window.scrollTo(%d,0)" % i)
    #             self.driver.execute_script(js_right)
    #             time.sleep(1)
    #             if self.driver.find_element(feature):
    #                 return self.driver.find_element(feature)
    #             else:
    #                 print("没找到")
    #             i += 200
    #
    #     else:
    #         raise Exception("滑动到底,没有找到")








