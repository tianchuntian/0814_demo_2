import unittest
from interface.login import Login
from common.op_database import OpDatabase


class Test_login(unittest.TestCase):
    """
    验证登录接口
    """
    # 绑定初始属性
    url = 'http://ecshop.itsoso.cn/ECMobile/?url=/user/signin'
    data = {"name": "李哈哈_5", "password": "123456"}

    def test_login(self):
        """
        验证登录接口是否正确
        :return:
        """
        # 获取登录返回值用户名
        res = Login(self.url).get_name(self.data)
        # 验证返回值是否与请求参数相同
        self.assertEqual(res, self.data['name'])


if __name__ == "__main__":
    unittest.main()
