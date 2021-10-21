import unittest
import time
import HTMLTestRunnerPlugins

# 确认用例存放路径
case_path = "./script"
# 将测试用例放入测试套件中
discover = unittest.defaultTestLoader.discover(case_path, pattern='test*.py')
# 执行用例并获取结果
# 确认执行结果存放路径
report_path = "./report"
# 获取时间
now = time.strftime("%Y_%m_%d %H-%M-%S")
# 编写结果的报告名
result_file = report_path + "/" + now + "report.html"
# 已写入二进制写入的方式打开文件
with open(result_file, "wb") as fp:
    runner = HTMLTestRunnerPlugins.HTMLTestRunner(
        title="ECShop项目web自动化测试报告",
        description="ECShop登录功能",
        stream=fp
    )
    runner.run(discover)
