from interface.collection_interface import Collection
from interface.login import Login
import unittest


class TestDeleteCollection(unittest.TestCase):
    def setUp(self) -> None:
        # 登录
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
        login = Login(url)
        data = {"name": "李哈哈_5", "password": "123456"}
        # 获取session
        self.res = login.get_session(data)
        # 获取商品red_id
        self.red_id = Collection.get_rec_id(self.res)

    def test_delete_collection(self):
        """测试用例,移除收藏商品"""
        # 获取数据库中收藏列表商品
        number1 = Collection.mysql_goods_number() - 1
        # 移除收藏商品
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/collect/delete"
        data = {'session': self.res, 'rec_id': f'{self.red_id}'}
        Collection.delete_collectioin(url, data)
        # 获取数据库中收藏列表商品
        number2 = Collection.mysql_goods_number()
        # 断言数据库商品是否一致
        self.assertEqual(number1, number2)


if __name__ == '__main__':
    unittest.main()
