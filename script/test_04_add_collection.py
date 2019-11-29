from interface.collection_interface import Collection
from interface.login import Login
import unittest



class TestAddCollection(unittest.TestCase) :
    def setUp(self) -> None:
        # 登录
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
        login = Login(url)
        data = {"name": "李哈哈_5", "password": "123456"}
        # 获取session
        self.res = login.get_session(data)
    def test_add_collection(self):
        """测试用例,增加收藏商品"""
        # 获取数据库中收藏列表商品
        number1 = Collection.mysql_goods_number()+1
        # 添加商品
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/collect/create"
        data = {"session":self.res,"goods_id":81}
        Collection.add_collection(url=url,data=data)
        # 获取添加后的数据库收藏商品种类
        number2 = Collection.mysql_goods_number()
        # 断言个数
        self.assertEqual(number1,number2)

if __name__ == '__main__':
    unittest.main()