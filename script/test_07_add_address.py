from interface.address_interface import Addresss
from interface.login import Login
import unittest


class TestAddAddress(unittest.TestCase):
    def setUp(self) -> None:
        # 登录
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
        login = Login(url)
        data = {"name": "李哈哈_5", "password": "123456"}
        # 获取session
        self.res = login.get_session(data)

    def test_add_address(self):
        """测试用例,添加收货地址"""
        # 获取数据库当前地址个数
        number1 = Addresss.get_mysql_adddress_number() + 1
        # 添加收货地址
        url1 = "http://ecshop.itsoso.cn/ECMobile/?url=/address/add"
        data1 = {"address": {"default_address": 0, "consignee": "小蒙", "tel": "18582361927", "zipcode": "656560",
                             "country": "1", "city": "271", "id": 0, "email": "123@163.com", "address": "天府新谷",
                             "province": "24", "district": "2716", "mobile": ""}, "session": self.res}
        Addresss.add_address(url=url1, data=data1)
        # 获取添加后的数据库收货地址个数
        number2 = Addresss.get_mysql_adddress_number()
        # 断言收货地址个数
        self.assertEqual(number1, number2)


if __name__ == '__main__':
    unittest.main()
