import time
import unittest

from script.test_enterprise_service import TestEnterpriseService
from script.test_help_center import TestHelpCenter
from script.test_intelligent_hardware import TestIntelligentHardware
from script.test_login import TestLogin
from script.test_translate import TestTranslate
from utils import DriverUtil
from tools.HTMLTestRunner import HTMLTestRunner
import config

# 关闭自动退出的开关
DriverUtil.set_auto_quit(False)

# 创建测试套件对象
suite = unittest.TestSuite()

# 添加测试用例
# suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestTranslate))
# suite.addTest(unittest.makeSuite(TestIntelligentHardware))
# suite.addTest(unittest.makeSuite(TestHelpCenter))
# suite.addTest(unittest.makeSuite(TestEnterpriseService))

# 执行测试套件
# unittest.TextTestRunner().run(suite)

# 指定测试报告路径
reprot_file = config.BASE_DIR + "/report/report{}.html".format(time.strftime("%Y%m%d-%H%M%S"))

# 打开文件流
with open(reprot_file, "wb") as f:
    # 创建HTMLTestRunner对象
    runner = HTMLTestRunner(f, title="iFlytek自动化测试报告", description="Win7.Chrome")

    # 执行测试套件
    runner.run(suite)

# 打开自动退出的开关
DriverUtil.set_auto_quit(True)

DriverUtil.quit_driver()
