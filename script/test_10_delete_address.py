from interface.address_interface import Addresss
from interface.login import Login
import unittest


class TestDeleteAddress(unittest.TestCase):
    def setUp(self) -> None:
        # 登录
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
        login = Login(url)
        data = {"name": "李哈哈_5", "password": "123456"}
        # 获取session
        self.res = login.get_session(data)
        # 获取address_id
        self.address_id = Addresss.get_address_id(self.res)

    def test_delete_address(self):
        """测试用例,删除地址"""
        # 获取数据库收货地址个数
        number1 = Addresss.get_mysql_adddress_number() - 1
        # 删除收货地址
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/address/delete"
        data = {"address_id": f"{self.address_id}", "session": self.res}
        Addresss.delete_address(url=url, data=data)
        # 获取数据库删除后收货地址的个数
        number2 = Addresss.get_mysql_adddress_number()
        # 断言
        self.assertEqual(number1, number2)


if __name__ == '__main__':
    unittest.main()
