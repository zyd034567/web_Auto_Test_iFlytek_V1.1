from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class TranslatePage(BasePage):
    """
    页-对象库层
    """

    def __init__(self):
        super().__init__()

        # 语音转文字
        self.speech_to_text = (By.XPATH, "//*[@id='menu_list']/li[2]/div/div[1]/div[1]/font/font")
        # 中文机器快转
        self.the_machine_runs_fast = (By.LINK_TEXT, "中文机器快转")
        # 中文人工精转
        self.chinese_manual_precision = (By.LINK_TEXT, "中文人工精转")
        # 英文机器快转
        self.english_machine_turn_fast = (By.LINK_TEXT, "英文机器快转")
        # 实时语音转文字
        self.real_time_voice_to_text = (By.LINK_TEXT, "实时语音转文字")

        # 多语种翻译
        self.multilingual_translation = (By.XPATH, "//*[@id='menu_list']/li[2]/div/div[2]/div[1]/font/font")
        # 人工翻译
        self.human_translation = (By.LINK_TEXT, "人工翻译")
        # 机器翻译
        self.machine_translation = (By.LINK_TEXT, "机器翻译")

    # 语音转文字
    def find_speech_to_text(self):
        return self.find_element(self.speech_to_text)

    # 中文机器快转
    def find_the_machine_runs_fast(self):
        return self.find_element(self.the_machine_runs_fast)

    # 中文人工精转
    def find_chinese_manual_precision(self):
        return self.find_element(self.chinese_manual_precision)

    # 英文机器快转
    def find_english_machine_turn_fast(self):
        return self.find_element(self.english_machine_turn_fast)

    # 实时语音转文字
    def find_real_time_voice_to_text(self):
        return self.find_element(self.real_time_voice_to_text)

    # 多语种翻译
    def find_multilingual_translation(self):
        return self.find_element(self.multilingual_translation)

    # 人工翻译
    def find_human_translation(self):
        return self.find_element(self.human_translation)

    # 机器翻译
    def find_machine_translation(self):
        return self.find_element(self.machine_translation)


class TranslateHandle(BaseHandle):
    """
    操作层
    """

    def __init__(self):
        self.translate_page = TranslatePage()

    # 检查"语音转文字"文本
    def select_speech_to_text(self):
        return self.translate_page.find_speech_to_text().text

    # 点击中文机器快转
    def click_the_machine_runs_fast(self):
        self.translate_page.find_the_machine_runs_fast().click()

    # 点击中文人工精转
    def click_chinese_manual_precision(self):
        self.translate_page.find_chinese_manual_precision().click()

    # 点击英文机器快转
    def click_english_machine_turn_fast(self):
        self.translate_page.find_english_machine_turn_fast().click()

    # 点击实时语音转文字
    def click_real_time_voice_to_text(self):
        self.translate_page.find_real_time_voice_to_text().click()

    # 检查"多语种翻译"文本
    def click_multilingual_translation(self):
        return self.translate_page.find_multilingual_translation().text

    # 点击人工翻译
    def click_human_translation(self):
        self.translate_page.find_human_translation().click()

    # 点击机器翻译
    def click_machine_translation(self):
        self.translate_page.find_machine_translation().click()


class TranslateProxy:
    """
    业务层
    """

    def __init__(self):
        self.translate_handle = TranslateHandle()

    # 获取"语音转文字"文本
    def gain_speech_to_text(self,expect):
        msg = self.translate_handle.select_speech_to_text()
        return expect == msg

    # 获取"多语种翻译"文本
    def gain_multilingual_translation(self,expect):
        msg = self.translate_handle.click_multilingual_translation()
        return expect == msg

    # 进入中文机器快转
    def access_the_machine_runs_fast(self):
        self.translate_handle.click_the_machine_runs_fast()

    # 进入中文人工精转
    def access_chinese_manual_precision(self):
        self.translate_handle.click_chinese_manual_precision()

    # 进入英文机器快转
    def access_english_machine_turn_fast(self):
        self.translate_handle.click_english_machine_turn_fast()

    # 进入实时语音转文字
    def access_real_time_voice_to_text(self):
        self.translate_handle.click_real_time_voice_to_text()

    # 进入人工翻译
    def access_click_human_translation(self):
        self.translate_handle.click_human_translation()

    # 进入机器翻译
    def access_click_machine_translation(self):
        self.translate_handle.click_machine_translation()





