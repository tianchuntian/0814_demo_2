from interface.address_interface import Addresss
from interface.login import Login
import unittest



class TestViewAddress(unittest.TestCase) :
    def setUp(self) -> None:
        # 登录
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
        login = Login(url)
        data = {"name": "李哈哈_5", "password": "123456"}
        # 获取session
        self.res = login.get_session(data)
    def test_view_address(self):
        """测试用例,查看地址"""
        # 查看收货地址
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/address/list"
        data = {"session":self.res}
        Addresss.view_address(url=url,data=data)
        # 获取当前地址数量
        number1 = Addresss.get_address_number(self.res)
        # 获取数据库的地址数量
        number2 = Addresss.get_mysql_adddress_number()
        # 断言
        self.assertEqual(number1,number2)


if __name__ == '__main__':
    unittest.main()