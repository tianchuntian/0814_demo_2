from interface.address_interface import Addresss
from interface.login import Login
from common.get_keyword import GetKeyword
import unittest



class TestModifyAddress(unittest.TestCase) :
    def setUp(self) -> None:
        # 登录
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
        login = Login(url)
        data = {"name": "李哈哈_5", "password": "123456"}
        # 获取session
        self.res = login.get_session(data)
        # 获取address_id
        self.address_id = Addresss.get_address_id(self.res)
    def test_modify_address(self):
        """测试用例,修改地址"""
        # 修改收货地址
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/address/update"
        data = {"address":{"default_address":0,"consignee":"user","tel":"1898976579464","zipcode":"621000","country":"4044","city":"0","id":0,"email":"98784564@qq.com","address":"sdfsdfsd","province":"0","district":"0","mobile":""},"address_id":f"{self.address_id}","session":self.res}
        # 获取预期结果
        expected = GetKeyword.get_keyword(data,"consignee")
        Addresss.modify_address(url=url, data=data)
        # 获取查看后的返回值
        url1 = "http://ecshop.itsoso.cn/ECMobile/?url=/address/list"
        data1 = {"session": self.res}
        result = Addresss.view_address(url1, data1)
        # 获取实际结果
        actual = GetKeyword.get_keyword(result,"consignee")
        # 断言前后的收货人是否一致
        self.assertEqual(expected,actual)

if __name__ == '__main__':
    unittest.main()