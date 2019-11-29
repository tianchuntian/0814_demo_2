from interface.goods_detail_interface import Goods_detail
from interface.login import Login
from common.get_keyword import GetKeyword
import unittest



class Test_goods_detail(unittest.TestCase):
    """
    验证商品详情接口
    """
    def setUp(self) -> None:
        # 登录数据
        login_url = 'http://ecshop.itsoso.cn/ECMobile/?url=/user/signin'
        login_data = {"name": "李哈哈_5", "password": "123456"}
        # 实例化登录对象
        login = Login(url=login_url)
        self.session = login.get_session(login_data)


    def test_goods_detail(self):
        data = {"goods_id": 89, "session": self.session}
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/goods"
        response = Goods_detail.goods_view(url=url, data=data)
        succeed = GetKeyword.get_keyword(response, 'succeed')
        goods_id = GetKeyword.get_keyword(response, 'id')
        result = True if goods_id == '89' else False
        self.assertEqual(succeed, result)



if __name__ == '__main__':
    unittest.main()
