import unittest
from interface.login import Login
from interface.goods_detail import GoodsDetail
from interface.shopping_car import ShoppingCar
from common.get_keyword import GetKeyword
from interface.address_interface import Addresss
from common.send_method import SendMethod
from common.op_database import OpDatabase



class TestShoppingProcess(unittest.TestCase) :
    def setUp(self) -> None:
        # 清空一下环境
        login = OpDatabase()
        login.clear_mysql()
    def test_shopping_process(self):
        """测试用例,购物流程"""
        # 1.登录,获取session和user_id
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
        login = Login(url)
        data = {"name":"李哈哈_5","password":"123456"}
        session = login.get_session(data)
        user_id = GetKeyword.get_keyword(session,"uid")
        # 2.添加收货地址
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/address/add"
        data = {"address":{"default_address":0,"consignee":"郭仁捷","tel":"18582361927","zipcode":"656560","country":"1","city":"271","id":0,"email":"1234@163.com","address":"天府新谷","province":"24","district":"2716","mobile":""},"session":session}
        Addresss.add_address(url, data)
        # 3.商品详情,获取商品的goods_id
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/goods"
        login = GoodsDetail(url)
        data = {"goods_id":89,"session":session}
        response = login.goods_detail(data)
        goods_id = GetKeyword.get_keyword(response,"id")
        # 4.添加到购物车
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/cart/create"
        login = ShoppingCar(url)
        data = {"spec":[],"session":session,"goods_id":goods_id,"number":1}
        login.add_shopping_car(data)
        # 5.确认订单
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/flow/checkOrder"
        data = {"session":session}
        SendMethod.send_method(url, data)
        # 6.提交订单
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/flow/done"
        data = {"shipping_id":"5","session":session,"pay_id":"4"}
        SendMethod.send_method(url, data)
        # 7.获取数据库中是否有订单
        try :
            db = OpDatabase()
            sql = f"select * from ecs_order_info where user_id={user_id}"
            result = db.get_one(sql)
        except :
            result = False
        # 8.断言
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()