from interface.collection_interface import Collection
from interface.login import Login
import unittest



class TestViewCollection(unittest.TestCase) :
    def setUp(self) -> None:
        # 登录
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
        login = Login(url)
        data = {"name": "李哈哈_5", "password": "123456"}
        # 获取session
        self.res = login.get_session(data)
    def test_view_collection(self):
        """测试用例,查看收藏商品列表"""
        # 查看收藏商品列表
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/collect/list"
        data = {"session":self.res,"pagination":{"count":10,"page":1},"rec_id":0}
        Collection.view_collection(url,data)
        # 获取当前收藏列表商品数量
        number1 = Collection.get_goods_number(self.res)
        # 获取数据库中收藏列表商品
        number2 = Collection.mysql_goods_number()
        # 断言两个个数是否一致
        self.assertEqual(number1,number2)

if __name__ == '__main__':
    unittest.main()