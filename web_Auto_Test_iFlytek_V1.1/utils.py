
from selenium import webdriver


class DriverUtil:
    _driver = None
    _auto_quit = True

    # 获取驱动对象，并完成初始化
    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(30)
            cls._driver.get("https://testbox.iflytek.com/")
        return cls._driver

    # 关闭驱动
    @classmethod
    def quit_driver(cls):
        if cls._auto_quit and cls._driver:
            cls._driver.quit()
            cls._driver = None

    # 设置是否自动退出
    @classmethod
    def set_auto_quit(cls, auto_quit):
        cls._auto_quit = auto_quit



